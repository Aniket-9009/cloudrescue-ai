import os
import warnings
import torch

from transformers import (
    AutoTokenizer,
    AutoConfig,
    Qwen3_5ForCausalLM,
    BitsAndBytesConfig,
)

from peft import PeftModel

from strands_decider.modeling import (
    StrandsDeciderModel,
    StrandsDeciderConfig,
    checkpoint_dir,
    config_path,
    load_head_state,
    build_head,
)

from strands_decider.infer import SystemOneEngine, EngineConfig
from strands_decider.schema import ChoiceQuestion


CHECKPOINT = "StrandsAgents/strands-decider-2B-hobson-v19"


def load_decider_4bit():

    print("\nStep 1: Loading Decider checkpoint...", flush=True)

    path = checkpoint_dir(CHECKPOINT)

    config = StrandsDeciderConfig.from_json(
        config_path(path)
    )

    print("Base model:", config.base_model, flush=True)

    print("\nStep 2: Loading Qwen model in 4-bit...", flush=True)

    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float32,
    )

    tokenizer = AutoTokenizer.from_pretrained(path)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    base_config = AutoConfig.from_pretrained(
        config.base_model
    )

    text_config = base_config.get_text_config()

    lm = Qwen3_5ForCausalLM.from_pretrained(
        config.base_model,
        config=text_config,
        quantization_config=quantization_config,
        device_map="cpu",
    )

    torso = lm.model
    del lm

    print("4-bit base model loaded!", flush=True)

    print("\nStep 3: Loading LoRA adapter...", flush=True)

    if config.use_lora:

        lora_path = os.path.join(path, "lora")

        if not os.path.isdir(lora_path):
            raise FileNotFoundError(
                f"LoRA adapter not found: {lora_path}"
            )

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")

            torso = PeftModel.from_pretrained(
                torso,
                lora_path,
                is_trainable=False,
            )

        missing_adapter_warnings = [
            str(item.message)
            for item in caught
            if "missing adapter keys" in str(item.message).lower()
        ]

        if missing_adapter_warnings:
            raise RuntimeError(
                "LoRA adapter weights did not load completely. "
                "Model decisions cannot be trusted until this is fixed.\n"
                + missing_adapter_warnings[0][:500]
            )

        print("LoRA adapter loaded without missing-key warnings!", flush=True)

    else:
        print("Checkpoint does not use LoRA.", flush=True)

    print("\nStep 4: Loading decision head...", flush=True)

    model = StrandsDeciderModel.__new__(
        StrandsDeciderModel
    )

    torch.nn.Module.__init__(model)

    model.config = config
    model.torso = torso
    model.tokenizer = tokenizer

    hidden_size = text_config.hidden_size

    print("Hidden size:", hidden_size, flush=True)

    model.head = build_head(
        config,
        hidden_size,
    )

    model.head.load_state_dict(
        load_head_state(path)
    )

    model.head.to(torch.float32)

    print("Decision head loaded!", flush=True)

    print("\nStep 5: Initializing decision engine...", flush=True)

    # Quantized models should not be moved using model.to().
    # The standard CPU initialization also upcasts the torso.
    # Therefore initialize the engine without those conversions.

    engine = SystemOneEngine.__new__(
        SystemOneEngine
    )

    engine.cfg = EngineConfig(device="cpu")
    engine.model = model.eval()
    engine.tok = tokenizer
    engine.device = "cpu"

    print("Engine initialized!", flush=True)

    return engine


def main():

    print("\n===================================")
    print("          CLOUDRESCUE AI")
    print("       STRANDS DECIDER 2B")
    print("===================================")

    engine = load_decider_4bit()

    print("\nStep 6: Testing AI tool selection...", flush=True)

    state = (
        "I cannot connect to my AWS EC2 instance using SSH."
    )

    questions = {
        "tool_selection": ChoiceQuestion(
            instructions=(
                "Select the best diagnostic tool for the "
                "user's AWS networking problem."
            ),
            criteria={
                "check_ssh": (
                    "Investigate EC2 SSH connection failures, "
                    "port 22, security groups, and SSH access."
                ),
                "check_internet": (
                    "Investigate internet connectivity, "
                    "route tables, NAT gateways, and "
                    "internet gateways."
                ),
            },
        )
    }

    print("\nUser Problem:", state, flush=True)
    print("Running Strands Decider 2B...", flush=True)

    with torch.inference_mode():
        response = engine.ask(
            state,
            questions,
        )

    print("\n========== AI DECISION ==========")
    print(response)
    print("=================================")


if __name__ == "__main__":
    main()