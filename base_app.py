import streamlit as st
from PIL import Image
import pandas as pd

# Set the title and layout of the app
st.set_page_config(
    page_title="Anime Recommender App",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Function to load images
def load_image(image_path):
    return Image.open(image_path)

# Load anime data
anime_data = pd.read_csv('anime.csv')

# Ensure required columns are present and fill NaNs with empty strings
if 'name' in anime_data.columns and 'genre' in anime_data.columns:
    anime_data['name'] = anime_data['name'].fillna('')
    anime_data['genre'] = anime_data['genre'].fillna('')
else:
    st.error("The required columns ('name' and 'genre') are not present in the dataset.")
    st.stop()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Recommend Anime", "Overview", "Insights", "Anime Archive", "About Us"])

# Recommend Anime page (now the first page)
if page == "Recommend Anime":
    # Load and display the logo
    st.image(load_image("images/Anime_recommender_logo.jpeg"), width=350)  # Adjust the width as needed

    st.title("Anime Recommender")
    st.subheader("Discover Your Next Anime Adventure with **AnimeXplore!**")
    st.image(load_image("images/Home_anime_collage.jpg"), width=1000)
    

    st.markdown("### Choose your recommendation method:")
    rec_method = st.selectbox("Recommendation Method", ["Content-Based Filtering", "Collaborative-Based Filtering"])

    if rec_method == "Content-Based Filtering":
        st.info("**Tell us what you like, and we'll suggest something you'll love!**")
        
        # User input for anime preferences
        genres = st.multiselect("Select your favorite genres:", 
                                ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", "Mystery", "Romance", "Sci-Fi", "Slice of Life"])
        st.slider("Select the rating range:", 1, 10, (1, 10))

        if st.button("Get Content-Based Recommendations"):
            st.success("Content-Based Recommendations would be displayed here based on your preferences!")
    
    elif rec_method == "Collaborative-Based Filtering":
        st.subheader("Collaborative-Based Filtering")
        st.info("**Discover Anime Loved by Fans Like You!**")
        # Placeholder for user ID input or other collaborative filtering mechanisms
        user_id = st.text_input("Enter your user ID:")
        
        if st.button("Get Collaborative-Based Recommendations"):
            st.success("Collaborative-Based Recommendations would be displayed here based on your user profile!")

# Overview page
elif page == "Overview":
    st.title("Welcome to our Anime Recommender App")
    st.info("**Proudly brought to you by AnimeXplore!**")
    st.image(load_image("images/Overview_banner.jpg"), width=1000)

    # Insert case study content
    st.subheader("Your Fun-Filled Anime Quest Begins")
    st.markdown("""
    Imagine a universe where every anime lover finds their perfect match, diving into captivating stories, unforgettable characters, and breathtaking adventures tailored to their unique tastes. At AnimeXplore, we’re on a mission to revolutionize how you discover anime by building a cutting-edge recommender system that’s as vibrant and dynamic as the anime titles it curates. Whether you're a seasoned otaku or a newcomer to the anime world, prepare to embark on an exhilarating journey through the ultimate anime discovery experience.

Anime, a unique form of animation originating from Japan, has a rich history that dates back to the early 20th century. From its humble beginnings with short, silent films, anime has evolved into a global phenomenon, captivating audiences with its diverse genres, intricate plots, and artistic brilliance. Notable milestones in anime history include the release of classics like "Astro Boy" in the 1960s, the rise of Studio Ghibli with timeless masterpieces such as "My Neighbor Totoro" and "Spirited Away," and the explosive popularity of series like "Naruto," "Attack on Titan," and "My Hero Academia."

The impact of anime on global pop culture is undeniable. It has not only entertained millions but also influenced fashion, music, and even technology. Conventions dedicated to anime, such as Anime Expo and Comic-Con, draw massive crowds, celebrating the community and creativity that anime fosters. Streaming platforms now host extensive libraries of anime, making it more accessible than ever before. The stories told through anime resonate deeply with fans, offering both escapism and reflection on real-world issues.
    """)

# Insights page
elif page == "Insights":
    st.title("Insights")
    st.info("**Explore Anime Insights and Statistics**")
    
    insights_option = st.selectbox("Choose an insight to view:", 
                                   ["Top 10 Most Rated Animes", "Top 10 Least Rated Animes", "Top 10 Anime Genre Distribution", "Distribution of User Ratings"])
    
    if insights_option == "Top 10 Most Rated Animes":
        st.image(load_image("images/top_10_most_rated_animes.png"), use_column_width=True)
    elif insights_option == "Top 10 Least Rated Animes":
        st.image(load_image("images/top_10_least_rated_animes.png"), use_column_width=True)
    elif insights_option == "Top 10 Anime Genre Distribution":
        st.image(load_image("images/top_10_anime_genre_distribution.png"), use_column_width=True)
    elif insights_option == "Distribution of User Ratings":
        st.image(load_image("images/distribution_of_user_ratings.png"), use_column_width=True)

# Anime Archive page
elif page == "Anime Archive":
    st.title("Anime Archive")
    st.info("**Explore the Vast Anime Collection🔥**")
    st.video("Anime_recommender_video.mp4")
    st.subheader("Search and explore our anime archive.")
    
    # Search bar for anime name or genre
    search_term = st.text_input("Search for anime by name or genre:")

    if search_term:
        filtered_data = anime_data[anime_data.apply(lambda row: search_term.lower() in row['name'].lower() or search_term.lower() in row['genre'].lower(), axis=1)]
        if not filtered_data.empty:
            for index, row in filtered_data.iterrows():
                st.header(row['name'])
                st.write(f"**Genres:** {row['genre']}")
                st.write(f"**Rating:** {row['rating']}/10")
        else:
            st.write("No anime found matching your search criteria.")

# About page
elif page == "About Us":
    st.title("About Us")
    st.subheader("Learn more about this app and its creators.")
    st.image(load_image("images/about_banner.jpg"), width=1000)

    st.markdown("""
    ### About This App:
    This Anime Recommender App is designed to help anime enthusiasts discover new shows to watch based on their preferences. 
    Whether you are a seasoned anime fan or just getting started, this app offers a wide range of features to enhance your anime-watching experience.
    
    ### About the Creators:
    We are a group of passionate anime fans and developers who aim to make anime discovery easier and more enjoyable. Feel free to reach out to us with any feedback or suggestions!
    """)
    # Meet Our Team section
    st.markdown("### Meet Our Team")
    st.markdown("""
    - **Clement Mphethi** - Lead Data Scientist
    - **Makhutjo Lehutjo** - Project Manager
    - **Prishani Kisten** - Github Manager
    - **Johannes Malefetsane Makgetha** - Data Scientist
    - **Lulama Nelson Mulaudzi** - Data Scientist
    """)
     # Contact Us section
    st.markdown("### Contact Us:")
    st.markdown("For inquiries, please contact us at [info@animexplore.com](mailto:info@animexplore.com).")

# Footer
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #637aba;
    text-align: center;
    padding: 10px;
}
</style>
<div class="footer">
    <p>&copy; 2024 Anime Recommender App | Designed with ❤️ by Anime Fans</p>
</div>
""", unsafe_allow_html=True)
