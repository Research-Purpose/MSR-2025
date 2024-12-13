import streamlit as st
import pandas as pd
import os
from PIL import Image

def load_data():
    # Load metadata
    metadata = pd.read_csv('Data/metadata.csv')
    
    # Load GPT-4 responses
    gpt4_df = pd.read_csv('Data/GPT-4o/llm_responses_combined.csv')
    
    return metadata, gpt4_df

# Dictionary of explanations for each ID
id_explanation = {
    79082901: "In this case GPT does a good job. The original post and GPT's response share the same fundamental concern about a warning message for an unused private variable in a Dart program. While keeping the core problem identical, GPT has restructured the question to be more comprehensive and easier to understand for the programming community.",
    79143869: "Here, both original and GPT response are related. The original post and GPT's response both address an issue with TailwindCSS @apply directives in a Vue project. While the original post is more technically specific with LSP details, GPT's response simplifies the issue to make it more accessible while maintaining the core problem.",
    79088829: "GPT's response is closely aligned with original post in this question. Both of them address a connection error when trying to use the Snowflake CLI. GPT's version takes the basic problem and expands it into a more detailed, actionable question by providing context about the configuration setup and suggesting potential areas to check.",
    79120973: "Here, GPT fails to capture the essense of user's question. The original post investigates a performance issue with Bulma CSS framework regarding z-index changes, while GPT's response misses the mark by addressing basic layout issues instead of the performance concerns.",
    79130607: "Here, GPT captures the general picture but not the specifics. Both posts focus on code coverage in Swift, but approach it differently. While the original post seeks specific exclusion techniques, GPT's broader approach to testing strategy and coverage improvement provides valuable perspective on the overall topic.",
    79045307: "Both the original post and GPT's response address viewing logcat messages in Android Studio's Run Console. While the original focuses on version-specific changes, GPT's response offers practical troubleshooting steps that could be helpful across versions."
}

def create_static_example(image_id, metadata_df, gpt4_df):
    # Get image path
    image_name = metadata_df[metadata_df['id'] == image_id]['image_name'].iloc[0]
    image_path = os.path.join("Data/images", image_name)
    
    # Get data
    example_data = gpt4_df[gpt4_df['Id'] == image_id].iloc[0]
    
    # Image Section
    st.markdown("## 📷 Image")
    try:
        image = Image.open(image_path)
        st.image(image, caption=f"Image ID: {image_id}", use_container_width=True)
    except Exception as e:
        st.error(f"Could not load image: {image_path}")
    
    st.markdown("---")
    
    # Content Section - Side by Side
    col1, col2 = st.columns(2)
    
    # Original Content
    with col1:
        st.markdown("## 📝 Original Content")
        with st.container():
            st.markdown("""
                <style>
                .original-content {
                    background-color: #e6f3ff;
                    padding: 5px;
                    border-radius: 3px;
                    height: 100%;
                }
                </style>
                """, unsafe_allow_html=True)
            st.markdown('<div class="original-content">', unsafe_allow_html=True)
            st.markdown("#### Title")
            st.write(example_data['Title'])
            st.markdown("#### Body")
            st.write(example_data['Body'])
            st.markdown('</div>', unsafe_allow_html=True)
    
    # GPT Response
    with col2:
        st.markdown("## 🤖 GPT Response")
        with st.container():
            st.markdown("""
                <style>
                .gpt-response {
                    background-color: #f0f7f0;
                    padding: 5px;
                    border-radius: 3px;
                    height: 100%;
                }
                </style>
                """, unsafe_allow_html=True)
            st.markdown('<div class="gpt-response">', unsafe_allow_html=True)
            st.markdown("#### Title")
            st.write(example_data['llm_cot_title'])
            st.markdown("#### Body")
            st.write(example_data['llm_cot_body'])
            st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Analysis Section
    st.markdown("## 💡 Analysis")
    with st.container():
        st.markdown("""
            <style>
            .explanation {
                background-color: #fff3e6;
                padding: 5px;
                border-radius: 3px;
            }
            </style>
            """, unsafe_allow_html=True)
        st.markdown('<div class="explanation">', unsafe_allow_html=True)
        st.write(id_explanation[image_id])
        st.markdown('</div>', unsafe_allow_html=True)

def main():
    st.title("Image Analysis Examples")
    
    # Load data
    metadata, gpt4_df = load_data()
    
    # List of example IDs
    example_ids = [79082901, 79143869, 79088829, 79130607, 79120973, 79045307]
    
    # Create dropdown for ID selection
    selected_id = st.selectbox(
        "Select an Image ID",
        example_ids,
        format_func=lambda x: f"Example ID: {x}"
    )
    
    st.markdown("---")
    
    # Display selected example
    create_static_example(selected_id, metadata, gpt4_df)

if __name__ == "__main__":
    main()