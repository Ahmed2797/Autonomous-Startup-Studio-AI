import streamlit as st
from auto_startup_ai.crew import AutoStartupAi

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AutoStartup AI",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🚀 AutoStartup AI")
st.caption("Autonomous Startup Builder powered by AI Agents")

st.markdown(
"""
Generate a **complete startup blueprint** automatically using multiple AI agents.

The system will:
- 🔎 Research emerging technology trends
- 📊 Analyze market opportunities
- 💡 Generate startup ideas
- 🛠 Design MVP product
- 📈 Create marketing & financial plans
- 🌐 Generate landing page
- 🎤 Build investor pitch deck
"""
)

st.divider()

# -----------------------------
# Input Section
# -----------------------------
col1, col2 = st.columns([2,1])

with col1:
    topic = st.text_input(
        "Startup Domain",
        placeholder="Example: AI Healthcare, Climate Tech, AI SaaS"
    )

with col2:
    run_button = st.button("🚀 Generate Startup")

st.divider()

# -----------------------------
# Run Crew
# -----------------------------
if run_button and topic:

    progress = st.progress(0)
    status = st.empty()

    try:
        status.info("Initializing AI agents...")
        progress.progress(10)

        crew_instance = AutoStartupAi().crew()

        status.info("Researching trends...")
        progress.progress(25)

        result = crew_instance.kickoff(inputs={"topic": topic})

        progress.progress(80)
        status.info("Compiling startup blueprint...")

        progress.progress(100)
        status.success("Startup generated successfully!")

        # -----------------------------
        # Result Tabs
        # -----------------------------
        tab1, tab2, tab3 = st.tabs([
            "📄 Startup Blueprint",
            "📊 Insights",
            "⬇ Download"
        ])

        with tab1:
            st.subheader("Startup Blueprint")
            st.markdown(result)

        with tab2:
            st.subheader("Generated Domain")
            st.write(topic)

            st.info(
                """
                This startup concept was generated using multiple AI agents
                working together through a structured pipeline.
                """
            )

        with tab3:
            st.download_button(
                label="Download Blueprint",
                data=result,
                file_name="startup_blueprint.md",
                mime="text/markdown"
            )

    except Exception as e:
        st.error(f"Error running AutoStartup AI: {e}")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("⚙️ AutoStartup AI")

st.sidebar.markdown(
"""
### 🤖 Agents in the System

- Trend Analyst  
- Market Research Analyst  
- Startup Strategist  
- VC Critic  
- Product Designer  
- Marketing Strategist  
- Financial Analyst  
- Tech Architect  
- Code Generator  
- Website Generator  
- Pitch Deck Generator  
- Report Generator
"""
)

st.sidebar.markdown("---")

st.sidebar.markdown(
"""
### 🧠 How it Works

AI agents collaborate to:

1. Discover trends  
2. Analyze markets  
3. Generate startup ideas  
4. Design products  
5. Build strategy and financial model
"""
)

st.sidebar.markdown("---")

st.sidebar.markdown(
"""
Built with:

- **CrewAI**
- **Streamlit**
- **LLM Agents**
"""
)

## streamlit run app.py