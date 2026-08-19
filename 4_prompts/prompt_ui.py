from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt
import os
import textwrap
import re


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Research Tool",
    page_icon="📚",
    layout="wide"
)


# =========================================================
# LOAD ENVIRONMENT
# =========================================================

load_dotenv()


# =========================================================
# HUGGING FACE MODEL
# =========================================================

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv(
        "HUGGINGFACEHUB_API_TOKEN"
    )
)

model = ChatHuggingFace(llm=llm)


# =========================================================
# CSS
# =========================================================

st.markdown(
    textwrap.dedent("""
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(99, 102, 241, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(139, 92, 246, 0.10),
                transparent 30%
            ),
            #0b0f19;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* HERO */

    .hero {
        text-align: center;
        margin-bottom: 3rem;
    }

    .hero-icon {
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(
            90deg,
            #818cf8,
            #c084fc,
            #f0abfc
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        line-height: 1.6;
        max-width: 680px;
        margin: auto;
    }


    /* SETTINGS */

    .settings-card {
        background: rgba(15, 23, 42, 0.80);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 18px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.20);
    }

    .settings-title {
        color: #f8fafc;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .settings-description {
        color: #94a3b8;
        font-size: 0.92rem;
    }


    /* SELECT BOX */

    div[data-baseweb="select"] > div {
        background-color: #111827 !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }


    /* LABEL */

    label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
    }


    /* BUTTON */

    .stButton > button {
        width: 100%;
        height: 3.3rem;
        border-radius: 12px;
        border: none;
        font-size: 1.05rem;
        font-weight: 700;
        color: white;
        background: linear-gradient(
            90deg,
            #6366f1,
            #8b5cf6
        );
        box-shadow:
            0 8px 25px rgba(99, 102, 241, 0.30);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow:
            0 12px 30px rgba(139, 92, 246, 0.40);
    }


    /* RESULT */

    .result-card {
        background: rgba(15, 23, 42, 0.80);
        border: 1px solid rgba(129, 140, 248, 0.20);
        border-radius: 18px;
        padding: 1.6rem;
        margin-top: 2rem;
        box-shadow:
            0 10px 40px rgba(0,0,0,0.20);
    }

    .result-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 1.2rem;
    }

    .result-icon {
        font-size: 1.6rem;
    }

    .result-title {
        font-size: 1.35rem;
        font-weight: 750;
        color: #f8fafc;
    }


    /* FOOTER */

    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 3rem;
        font-size: 0.85rem;
    }

    </style>
    """),
    unsafe_allow_html=True
)


# =========================================================
# HERO
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="hero">
        <div class="hero-icon">📚</div>
        <div class="hero-title">Research Tool</div>
        <div class="hero-subtitle">
            Understand complex research papers with
            AI-powered explanations tailored to your
            preferred style and depth.
        </div>
    </div>
    """),
    unsafe_allow_html=True
)


# =========================================================
# SETTINGS CARD
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="settings-card">
        <div class="settings-title">
            ⚙️ Research Settings
        </div>

        <div class="settings-description">
            Choose a research paper and customize how
            you want the explanation to be generated.
        </div>
    </div>
    """),
    unsafe_allow_html=True
)


# =========================================================
# INPUTS
# =========================================================

col1, col2, col3 = st.columns(3)


with col1:

    paper_input = st.selectbox(
        "📄 Research Paper",
        [
            "Attention Is All You Need",
            "BERT: Pre-training of Deep Bidirectional Transformers",
            "GPT-3: Language Models are Few-Shot Learners",
            "Diffusion Models Beat GANs on Image Synthesis"
        ]
    )


with col2:

    style_input = st.selectbox(
        "🎨 Explanation Style",
        [
            "Beginner-Friendly",
            "Technical",
            "Code-Oriented",
            "Mathematical"
        ]
    )


with col3:

    length_input = st.selectbox(
        "📏 Explanation Length",
        [
            "Short (1-2 paragraphs)",
            "Medium (3-5 paragraphs)",
            "Long (detailed explanation)"
        ]
    )


# =========================================================
# GENERATE BUTTON
# =========================================================

st.write("")

if st.button("✨ Generate Explanation"):

    # Load your existing template.json

    template = load_prompt("template.json")

    # LangChain chain

    chain = template | model

    # Generate

    with st.spinner("🔬 Analyzing the research paper..."):

        result = chain.invoke(
            {
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input
            }
        )


    # =====================================================
    # CLEAN MODEL OUTPUT
    # =====================================================

    answer = result.content

    # Remove accidental HTML if model produces it

    answer = re.sub(
        r"</?div[^>]*>",
        "",
        answer,
        flags=re.IGNORECASE
    )

    answer = re.sub(
        r"</?(span|section|article|header|footer)[^>]*>",
        "",
        answer,
        flags=re.IGNORECASE
    )

    answer = answer.strip()


    # =====================================================
    # RESULT HEADER
    # =====================================================

    st.markdown(
        textwrap.dedent("""
        <div class="result-card">
            <div class="result-header">
                <div class="result-icon">🧠</div>
                <div class="result-title">
                    AI Explanation
                </div>
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )


    # =====================================================
    # AI RESPONSE
    # =====================================================

    st.markdown(answer)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    textwrap.dedent("""
    <div class="footer">
        Powered by LangChain • Hugging Face • Qwen
    </div>
    """),
    unsafe_allow_html=True
)