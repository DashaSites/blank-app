import streamlit as st
import pandas as pd
import folium
from streamlit.components.v1 import html
import numpy as np


st.header('Let stars shine brighter :star: :star: :telescope: ')

## INTRO: WHAT IS THIS PAGE ABOUT
st.write('We are creations of stars, and the stars are projecting our lives down to the planet Earth. But what do we know about them? You’ve come to the right place to see more meaning in their beauty and to understand how they affect you. Enjoy!')
st.write(' ')

## LOOK AT THE STARS
st.subheader('Look up at the Big Sky')
starsImage = 'https://cdn.mos.cms.futurecdn.net/6LdSCQWb6pNajdRopNG3h8-1200-80.jpeg.webp'
st.image(starsImage, caption='Somewhere in the Small Magellanic Cloud galaxy / NASA')
st.write('The observable universe contains approximately 2 trillion galaxies, each with a vast number of stars. Estimates suggest there are around 100 to 200 billion stars in our Milky Way galaxy alone. Beyond our observable universe, the total number of universes is unknown, but current theories and models suggest that our universe could be one of many in a potentially vast multiverse.')
st.write(' ')

## LOOK INSIDE HUBBLE
st.subheader('Look inside Hubble')
st.write('The Hubble Space Telescope, our window to the stars, has been operating in orbit for over 30 years. It has peered back 13.3 billion years into the past and captured images of cosmic objects that formed just 500 million years after the Big Bang. Take a look at how the Hubble itself is constructed.')
VIDEO_URL = 'https://youtu.be/XZ_WeTGCU9o'
st.video(VIDEO_URL)

## MAP WITH ATTRACTIONS
st.write(' ')
st.write(' ')
st.subheader('Visit these spots to get an eyeful of stars')
# Creating the map
google_maps_url = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}'
m = folium.Map(
    location=[32.0700087148174, 34.816067387030174],
    zoom_start=7,
    tiles=google_maps_url,
    attr='Map tiles by <a href="https://developers.google.com/maps/documentation/javascript/overview">Google Maps</a>'
)

# Adding markers with captions
locations = [
    {"name": "Givatayim observatory", "lat": 32.0700087148174, "lon": 34.816067387030174},
    {"name": "Bareket observatory", "lat": 31.892393036340785, "lon": 35.037921288235204},
    {"name": "Ramon Crater telescope tours", "lat": 30.61983575896422, "lon": 34.80445146313616},
    {"name": "Cosmos Telescope store", "lat": 32.0868603268629, "lon": 34.82102552175639},
    {"name": "Stern Stargazing point", "lat": 30.624367069827265, "lon": 34.83111862283641},
    {"name": "Astrofan Mobile observatory", "lat": 30.568318144821795, "lon": 34.89463606108496},
    {"name": "Planetarium", "lat": 30.623065915863585, "lon": 34.806899147482696},
    {"name": "Bareket Telescope store", "lat": 31.89839308437534, "lon": 35.058532061337615},
    {"name": "Israel National Museum of Science, Technology, and Space", "lat": 32.81042306350289, "lon": 34.99658118614289}
]

for location in locations:
    folium.Marker(
        location=[location["lat"], location["lon"]],
        popup=folium.Popup(location["name"], parse_html=True)
    ).add_to(m)

# Rendering the map
st.write('If you are hungry for astronomic delights, click on the markers on the map and set off for new experiences!')
st.components.v1.html(m._repr_html_(), height=500)

## СONSTELLATION SELECTBOX
st.subheader('7 most famous constellations')
st.write('Constellations are patterns of stars in the night sky that have been recognized and named by various cultures throughout history. These celestial groupings not only serve as a way to map the heavens but also hold significant cultural, mythological, and navigational importance. Click on a constellation to get familiar with it.')
# st.selectbox('Select from the dropdown list:', options=('Orion', 'Ursa Major', 'Ursa Minor', 'Cassiopeia', 'Scorpius', 'Leo', 'Taurus'))

# Creating a dictionary with constellations data
constellations = {
    'Orion': {
        'image_url': 'https://media.gettyimages.com/id/1130628633/vector/orion-star-constellation.jpg?s=612x612&w=0&k=20&c=IFLwgZpUVK-jgoXPAlAfewzi5yuZK6STKh_YGcc09Dk=',
        'description': 'Orion is one of the most prominent and recognizable constellations in the night sky, named after the mythical Greek hunter Orion. Its discovery is not attributed to a single individual but rather to the ancient cultures who first observed and named it thousands of years ago. Orion is often depicted in mythology as a giant hunter, and his story features prominently in various mythologies, including those of the Greeks, Egyptians, and Babylonians. According to Greek legend, Orion was a skilled hunter who was placed among the stars by Zeus after his death. This constellation is home to some of the brightest stars visible from Earth, including Betelgeuse, a red supergiant marking Orions right shoulder, and Rigel, a blue supergiant representing his left foot. The most recognizable feature of Orion is the Orions Belt, a straight line of three bright stars—Alnitak, Alnilam, and Mintaka—that form the hunters belt. Orion is best visible in the evening during the winter months in the Northern Hemisphere, typically from November to February. It is most prominent in regions with clear winter skies, such as North America and Europe. In the Southern Hemisphere, Orion is visible during summer and early autumn. Its visibility and bright stars make Orion a favorite target for stargazers and astronomers alike, and its prominent position in the sky has made it a significant feature in the folklore and scientific studies of various cultures throughout history.'
    },
    'Ursa Major': {
        'image_url': 'https://media.gettyimages.com/id/1130628809/vector/ursa-major-star-constellation.jpg?s=612x612&w=0&k=20&c=jNnwOayN48LEzCDh8siH4wdbW7eLs-EiHjKVJ7fFowc=',
        'description': 'Ursa Major, also known as the Great Bear, is one of the most recognizable constellations in the night sky, particularly famous for its prominent asterism, the Big Dipper. The constellations name and its mythological significance trace back to ancient cultures, including the Greeks, Romans, and Babylonians. In Greek mythology, Ursa Major is often associated with the nymph Callisto, who was transformed into a bear and then placed among the stars by Zeus. Ursa Major contains seven bright stars that form the distinctive shape of the Big Dipper, which has been used for centuries as a navigational aid. The stars of the Big Dipper include Alkaid, Mizar, Alioth, Megrez, Phecda, Dubhe, and Merak. This asterism is particularly useful for locating the North Star, Polaris, as the two outer stars of the Big Dippers bowl point directly towards it. Visible throughout the year in the Northern Hemisphere, Ursa Major is most prominent during the spring and summer months, although its visibility can vary depending on the observers latitude. In the Southern Hemisphere, it is less visible, though it can sometimes be seen in the southernmost regions.'
    },
    'Ursa Minor': {
        'image_url': 'https://media.gettyimages.com/id/1130628822/vector/ursa-minor-star-constellation.jpg?s=612x612&w=0&k=20&c=377c6eNju-rzuwjZ-qb6RBDx0TccSdy7MoVHB4KTBNE=',
        'description': 'Ursa Minor, also known as the Little Bear, is a prominent constellation in the northern sky. It is best known for containing the North Star, Polaris, which has been a crucial navigational aid for centuries. The constellations name and its depiction have roots in various ancient mythologies, including Greek, Roman, and Nordic traditions. In Greek mythology, Ursa Minor is often associated with the nymph Arcas, who, along with his mother Callisto, was transformed into a bear by Zeus and placed in the sky to protect them. Ursa Minor is most famous for its asterism, the Little Dipper, which is composed of seven stars that outline the shape of a small dipper or ladle. The key stars in this asterism are Polaris, the brightest star and the current North Star, along with Kochab, Pherkad, and others. Polaris holds a unique position near the celestial north pole, making it an essential point of reference for navigation. The constellation is visible throughout the year in the Northern Hemisphere and is most prominent during the summer and fall months. Its location near the north celestial pole means that it remains above the horizon for most observers in the Northern Hemisphere, making it a consistent feature of the night sky.'
    },
    'Cassiopeia': {
        'image_url': 'https://media.gettyimages.com/id/1130628583/vector/cassiopeia-star-constellation.jpg?s=612x612&w=0&k=20&c=-g2V8c44SP9eFIVVCqBd8H-kbKkZb2zUYAtHMErDAc8=',
        'description': 'Cassiopeia is easily recognizable by its distinctive W shape, which is formed by five bright stars. This constellation is named after the vain queen Cassiopeia from Greek mythology, who was the wife of King Cepheus and the mother of Andromeda. According to myth, Cassiopeia boasted about her beauty, claiming that she was more beautiful than the Nereids, sea nymphs. This arrogance led to her being punished by being placed among the stars, where she is depicted sitting on a throne. The constellation of Cassiopeia is notable for containing several interesting celestial objects. Among these is the star Schedar, which is the brightest star in the constellation and represents the queens chest. Cassiopeia also hosts the Messier 103 (M103), a well-known open star cluster, and several other notable deep-sky objects. Cassiopeia is circumpolar for observers in the Northern Hemisphere, meaning it is visible throughout the year and never sets below the horizon. Its visibility is particularly strong in autumn and winter, making it a prominent feature of the night sky during these seasons. Its unique W shape and bright stars make it an easy constellation to identify, even in areas with light pollution.'
    },
    'Scorpius': {
        'image_url': 'https://media.gettyimages.com/id/1130628768/vector/scorpius-star-constellation.jpg?s=612x612&w=0&k=20&c=05B1AFOKZd75f21oDlLMDi7q7KmfA0v36Rwo1-Sgglo=',
        'description': 'Scorpius, or Scorpio, is representing a scorpion in Greek mythology. It is one of the twelve constellations of the zodiac and is easily identifiable due to its distinctive hook-shaped pattern, which resembles the curved tail of a scorpion. According to myth, Scorpius was sent by the Earth goddess Gaia to kill the hunter Orion, who had boasted about his ability to hunt any animal. The battle between Orion and Scorpius was so intense that both were placed in the sky by Zeus, with Scorpius rising in the east as Orion sets in the west, ensuring they would never be seen together in the night sky. Scorpius is home to several notable celestial objects, including some of the brightest stars visible from Earth. Antares, the constellations brightest star, is a red supergiant located at the heart of the scorpion, often referred to as the "rival of Mars" due to its reddish appearance. The constellation also contains the Messier 4 (M4), a prominent globular star cluster, and the Messier 7 (M7), an open star cluster known for its rich collection of stars. In terms of visibility, Scorpius is best observed during the summer months in the Northern Hemisphere, and it is prominently visible from late spring through early autumn.'
    },
    'Leo': {
        'image_url': 'https://media.gettyimages.com/id/1130628624/vector/leo-star-constellation.jpg?s=612x612&w=0&k=20&c=AWlUiEXK--5RVuyQip2wQciREFoWpIBZTOG7Rs044eE=',
        'description': 'Leo is a prominent constellation of the zodiac, located in the northern hemispheres sky. Its name and shape represent a lion, an iconic symbol in various cultures and mythologies. In Greek mythology, Leo is often associated with the Nemean Lion, a fearsome beast slain by the hero Heracles (Hercules) as one of his Twelve Labors. The constellations depiction as a lion is symbolic of strength and bravery, reflecting its association with the lions regal nature and formidable presence. The constellation of Leo is notable for its bright and easily recognizable stars. Regulus, the constellations brightest star, represents the lions heart and is one of the brightest stars in the night sky. Another significant star is Denebola, which marks the lions tail. Leo also contains several interesting deep-sky objects, including the Leo Triplet, a trio of interacting galaxies that are popular targets for amateur astronomers. Leo is best visible in the evening sky during the spring months in the Northern Hemisphere, particularly from late March to June.'
    },
    'Taurus': {
        'image_url': 'https://media.gettyimages.com/id/1130628795/vector/taurus-star-constellation.jpg?s=612x612&w=0&k=20&c=wpeF6PLL6nFsV0_R8DuNgeXHtsJvcd_1nu7lfPTRwps=',
        'description': 'Taurus is a prominent constellation in the night sky, representing a bull in various mythological traditions. It is one of the twelve constellations of the zodiac and is notable for its significant role in both ancient and modern astronomy. In Greek mythology, Taurus is often associated with the story of Zeus, who transformed himself into a bull to abduct Europa, a Phoenician princess. The constellations shape and placement in the sky symbolize the strength and majesty of the bull. Taurus is home to several noteworthy celestial objects. The constellations most famous feature is the Pleiades star cluster, also known as the Seven Sisters, which is a group of young, hot stars that are easily visible to the naked eye. Another prominent feature is the Hyades star cluster, which forms the V-shaped pattern of the bulls head and is one of the nearest open clusters to Earth. The brightest star in Taurus is Aldebaran, a red giant that represents the bulls eye and is one of the brightest stars in the night sky. Taurus is best visible in the evening sky from November to April, making it a key constellation during the winter months in the Northern Hemisphere. It is also observable in the early morning hours during the summer months in the Southern Hemisphere.'
    }
}

selected_constellation = st.selectbox(
    'Select from the dropdown list:',
    options=list(constellations.keys())
)

# Choosing content based on the selected option
def display_constellation_info(constellation_name):
    if constellation_name in constellations:
        st.subheader(constellation_name)
        st.image(constellations[constellation_name]['image_url'])
        st.write(constellations[constellation_name]['description'])

# Displaying the selected constellation's info
display_constellation_info(selected_constellation)





## SODIZAC SIGNS RADIOBUTTONS
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")






## FEEDBACK
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write("How did you like this page?")
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"Thanks for the feedback!")