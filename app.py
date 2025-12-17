import streamlit as st
from datetime import datetime

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Amr ❤️",
    page_icon="❤️",
    layout="wide"
)

# ------------------ Custom CSS ------------------
st.markdown(
    """
    <style>
    body {
        background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
        color: #ffffff;
        font-family: 'Helvetica', sans-serif;
    }

    /* Falling hearts */
    .hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 0;
    }
    .heart {
        position: absolute;
        top: -40px;
        font-size: 40px;
        color: rgba(255, 105, 180, 0.95);
        animation: fall linear infinite;
    }
    @keyframes fall {
        from { transform: translateY(-50px) translateX(0); opacity: 1; }
        to { transform: translateY(120vh) translateX(150px); opacity: 0; }
    }

    .title {
        font-size: 72px;
        font-weight: 900;
        text-align: center;
        margin-top: 30px;
        color: #ffdde1;
        text-shadow: 3px 3px 20px #ff6f91;
    }
    .subtitle {
        font-size: 28px;
        text-align: center;
        color: #f8cdda;
        margin-bottom: 120px;
        line-height: 1.6;
        text-shadow: 1px 1px 6px #ff6f91;
    }

    .card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        padding: 50px;
        border-radius: 32px;
        margin-bottom: 60px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.45);
        border: 2px solid rgba(255,105,180,0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0 25px 60px rgba(0,0,0,0.6);
    }

    .section-title {
        font-size: 42px;
        margin-bottom: 25px;
        color: #fff5f7;
    }

    .soft-text {
        font-size: 30px;
        line-height: 2.6;
        color: #ffe4ec;
    }

    .soft-text li {
        margin-bottom: 25px;
        list-style: none;
    }
    .soft-text li:before {
        content: '❤️';
        margin-right: 15px;
        color: #ff6f91;
    }

    .footer {
        text-align: center;
        color: #ffb6c1;
        margin: 140px 0 60px;
        font-size: 28px;
        line-height: 2;
        text-shadow: 1px 1px 5px #ff6f91;
    }

    .stImage img {
        border-radius: 32px;
        box-shadow: 0 15px 45px rgba(0,0,0,0.6);
        max-width: 100%;
        transition: transform 0.3s ease;
        margin-top: 15px;
    }
    .stImage img:hover {
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ Falling Hearts ------------------
st.markdown(
    """
    <div class="hearts">
        <div class="heart" style="left:10%; animation-duration:5s;">❤️</div>
        <div class="heart" style="left:25%; animation-duration:6s;">❤️</div>
        <div class="heart" style="left:40%; animation-duration:4.5s;">❤️</div>
        <div class="heart" style="left:55%; animation-duration:6.5s;">❤️</div>
        <div class="heart" style="left:70%; animation-duration:5.5s;">❤️</div>
        <div class="heart" style="left:85%; animation-duration:7s;">❤️</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------ Header ------------------
st.markdown("<div class='title'>To the Man I Love ❤️</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>A little digital universe made just for you — End of 2025</div>", unsafe_allow_html=True)

# ------------------ Helper for Sections ------------------
def section(image_url, title, bullet_points):
    st.markdown("<hr style='border:2px solid rgba(255,105,180,0.4); margin:80px 0;'>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1], gap="small")
    with col1:
        # st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
        st.markdown(f"<ul class='soft-text'>{bullet_points}</ul>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.image(image_url, width=500)



# ------------------ Sections ------------------
section(
    "data/Amr.jpeg",
    "✨ What You Built This Year",
    """
    <li>Left a stable job to pursue your dreams</li>
    <li>Proven yourself in your new career</li>
    <li>Learned Java, Spring Boot, SQL, and more</li>
    <li>Learning new skills every day</li>
    <li>Studying microservices</li>
    <li>Started Data Structures course</li>
    <li>Almost finished SQL course</li>
    <li>Consistent with prayers</li>
    <li>Listening to Quran regularly</li>
    <li>Taking care of health and fitness</li>
    <li>Tracking expenses for better finances</li>
    <li>Quit vaping, proud of you</li>
    """
)

section(
    "data/whats/Amr_2.jpeg",
    "❤️ The Things I Love About You",
    """
    <li>Your kindness and big heart</li>
    <li>Your strength and masculinity</li>
    <li>Your deep care and making me feel special</li>
    <li>Your sense of humor</li>
    <li>Your intelligence and wisdom</li>
    <li>Your ambition</li>
    <li>Making everything better just by being there</li>
    <li>I love you for being you</li>
    """
)

section(
    "data/us.jpeg",
    "🌱 How You Changed My Life",
    """
    <li>You made life feel safer</li>
    <li>You make me feel more feminine</li>
    <li>Supported me in ways I never imagined</li>
    <li>Main reason to wear hijab with confidence and happiness</li>
    <li>Your existence is rizq I am grateful for</li>
    """
)

# ------------------ Footer ------------------
year = datetime.now().year
st.markdown(f"<div class='footer'>I am sure, insha'alah will achieve all your dreams very soon, my love. And before the end of 2026, we will be together in our home, married, living our life blessed by Allah and our prayers, filling every moment with love ❤️</div>", unsafe_allow_html=True)
