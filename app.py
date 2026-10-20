import time
import torch
import streamlit as st

from strands_decider.schema import ChoiceQuestion

from decider_4bit import load_decider_4bit

from diagnostic_tools import (
    DIAGNOSTIC_TOOLS,
    TOOL_DESCRIPTIONS,
)


# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="CloudRescue AI",
    page_icon="☁️",
    layout="centered",
)


# =====================================
# LOAD STRANDS DECIDER 2B
# =====================================

@st.cache_resource(show_spinner=False)
def load_ai_model():

    return load_decider_4bit()


# =====================================
# AI TOOL SELECTION
# =====================================

def select_tool_with_ai(engine, problem):

    questions = {
        "tool_selection": ChoiceQuestion(
            instructions=(
                "Select exactly one diagnostic tool "
                "that best matches the user's AWS "
                "networking problem."
            ),

            criteria=TOOL_DESCRIPTIONS,
        )
    }

    with torch.inference_mode():

        response = engine.ask(
            problem,
            questions,
        )

    answer = response.answers["tool_selection"]

    return (
        answer.choice,
        answer.confidence,
        answer.probabilities,
    )


# =====================================
# HEADER
# =====================================

st.title("☁️ CloudRescue AI")

st.subheader("AWS Troubleshooting Assistant")

st.write(
    "Diagnose AWS networking problems using "
    "Strands Decider 2B."
)

st.info(
    "🧠 AI Engine: Strands Decider 2B "
    "(4-bit quantized, running locally on CPU)"
)

st.caption(
    "Supports 3 simulated AWS diagnostic tools."
)


# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.header("☁️ CloudRescue AI")

    st.write("**AI Model:** Strands Decider 2B")

    st.write("**Inference:** Local CPU (4-bit)")

    st.write("**Diagnostic Tools:** 3")

    st.write("**Mode:** Simulation")

    st.divider()

    st.subheader("Available Tools")

    for tool_name in DIAGNOSTIC_TOOLS:

        st.write(f"• `{tool_name}`")


# =====================================
# USER INPUT
# =====================================

problem = st.text_area(
    "Describe your AWS problem:",

    placeholder=(
        "Example: My EC2 SSH connection is not working."
    ),

    height=130,
)

diagnose = st.button(
    "🔍 Diagnose Problem",
    type="primary",
    use_container_width=True,
)


# =====================================
# DIAGNOSIS
# =====================================

if diagnose:

    if not problem.strip():

        st.warning(
            "Please describe your AWS problem."
        )

    else:

        try:

            total_start = time.perf_counter()

            # ---------------------------------
            # STEP 1: LOAD MODEL
            # ---------------------------------

            load_start = time.perf_counter()

            with st.spinner(
                "Loading Strands Decider 2B..."
            ):

                engine = load_ai_model()

            load_time = (
                time.perf_counter() - load_start
            )

            # ---------------------------------
            # STEP 2: AI DECISION
            # ---------------------------------

            decision_start = time.perf_counter()

            with st.spinner(
                "AI is selecting the diagnostic tool..."
            ):

                selected_tool, confidence, probabilities = (
                    select_tool_with_ai(
                        engine,
                        problem,
                    )
                )

            decision_time = (
                time.perf_counter() - decision_start
            )

            # ---------------------------------
            # STEP 3: EXECUTE TOOL
            # ---------------------------------

            if selected_tool not in DIAGNOSTIC_TOOLS:

                st.warning(
                    "Unsupported tool selected."
                )

                st.stop()

            tool_start = time.perf_counter()

            result = DIAGNOSTIC_TOOLS[
                selected_tool
            ]()

            tool_time = (
                time.perf_counter() - tool_start
            )

            total_time = (
                time.perf_counter() - total_start
            )

            # ---------------------------------
            # AI DECISION RESULT
            # ---------------------------------

            st.success(
                "AI decision completed successfully!"
            )

            st.write("### 🧠 AI Decision")

            st.write(
                "**Selected Tool:**",
                f"`{selected_tool}`",
            )

            st.metric(
                "Decision Confidence",
                f"{confidence * 100:.1f}%",
            )

            # ---------------------------------
            # TOOL PROBABILITIES
            # ---------------------------------

            with st.expander(
                "📊 Tool Selection Probabilities"
            ):

                sorted_probabilities = sorted(
                    probabilities.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )

                for tool_name, probability in sorted_probabilities:

                    st.write(
                        f"**{tool_name}:** "
                        f"{probability * 100:.2f}%"
                    )

                    st.progress(
                        min(
                            max(float(probability), 0.0),
                            1.0,
                        )
                    )

            # ---------------------------------
            # DIAGNOSTIC RESULT
            # ---------------------------------

            st.write("### 🔍 Diagnostic Result")

            st.info(
                f"Running `{selected_tool}`..."
            )

            if result["status"] == "success":

                st.success(result["message"])

            elif result["status"] == "warning":

                st.warning(result["message"])

            else:

                st.error(result["message"])

            # ---------------------------------
            # FINDING
            # ---------------------------------

            st.write("### 🔎 Finding")

            st.write(result["finding"])

            # ---------------------------------
            # RECOMMENDATION
            # ---------------------------------

            st.write("### 💡 Recommendation")

            st.markdown(result["recommendation"])

            st.caption(
                "This result is based on simulated "
                "AWS configuration."
            )

            # ---------------------------------
            # PERFORMANCE MONITORING
            # ---------------------------------

            st.divider()

            st.write("### ⚡ Performance Monitoring")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Model Loading Time",
                    f"{load_time:.2f} sec",
                )

                st.metric(
                    "Diagnostic Tool Time",
                    f"{tool_time:.4f} sec",
                )

            with col2:

                st.metric(
                    "AI Decision Time",
                    f"{decision_time:.2f} sec",
                )

                st.metric(
                    "Total Response Time",
                    f"{total_time:.2f} sec",
                )

        except Exception as error:

            st.error(
                "An error occurred during AI diagnosis."
            )

            st.exception(error)


# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    "CloudRescue AI | Powered by Strands Decider 2B"
)

st.caption(
    "Educational simulator — does not inspect "
    "real AWS resources."
)