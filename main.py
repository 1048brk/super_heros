import streamlit as st
import requests

# Title and description
st.title("Superhero Search Application")
st.write("Find detailed information about your favorite superheroes!")

# Input for superhero name
hero_name = st.text_input("Enter the name of a superhero:")
if st.button("Search"):
    # SuperHero API URL
    api_url = f"https://superheroapi.com/api/6e0f688aa393865955a795e87e5705bb/search/{hero_name}"

    # Send request to API
    response = requests.get(api_url)

    if response.status_code == 200:
        # Get the data from API response
        data = response.json()

        if data["response"] == "success":
            st.write(f"**Results for {hero_name}:**")

            # Display information for each hero in the results
            for hero in data["results"]:
                st.subheader(hero["name"])

                # Organize information into a table
                st.write("### Hero Information")
                st.table({
                    "Attribute": [
                        "Full Name",
                        "Aliases",
                        "Place of Birth",
                        "First Appearance",
                        "Gender",
                        "Weight",
                        "Height",
                        "Relatives",
                    ],
                    "Value": [
                        hero["biography"]["full-name"] or "Unknown",
                        ", ".join(hero["biography"]["aliases"]) or "None",
                        hero["biography"]["place-of-birth"] or "Unknown",
                        hero["biography"]["first-appearance"] or "Unknown",
                        hero["appearance"]["gender"] or "Unknown",
                        hero["appearance"]["weight"][1] or "Unknown",
                        hero["appearance"]["height"][1] or "Unknown",
                        hero["connections"]["relatives"] or "Unknown",
                    ],
                })

                # Display hero image
                st.write("### Hero Image")
                st.image(hero["image"]["url"], width=300)
        else:
            st.write("No superhero found with this name.")
    else:
        st.write("Error connecting to the API.")
