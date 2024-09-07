import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from streamlit_gsheets import GSheetsConnection

name_dict = {
    "x": 40,
    "y": 70,
    "max_width": 100,
    "font_size": 40,
}

description_dict = {
    "x": 120,
    "y": 70,
    "max_width": 100,
    "font_size": 20,
}

effect_dict = {
    "x": 200,
    "y": 70,
    "max_width": 100,
    "font_size": 20,
}

# Usage example of text on image
image_path = "potion_background.jpg"  # Replace with the actual path to your image file
text = "Potion of Power"
output_path = "output.jpg"  # Replace with the desired output path


def add_text_to_image(image_path, text, output_path, x_pos, y_pos):
    # Open the image
    image = Image.open(image_path)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define the font size and font path
    font_size = 40
    font_path = "dungeon_font.TTF"  # Replace with the actual path to your font file

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Calculate the position to place the text
    text_width, text_height = draw.textsize(text, font=font)
    x = x_pos  # (image.width - text_width) // 2
    y = y_pos - text_height
    print(f"Text width: {image.height}, Text height: {text_height}")
    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=(0, 0, 0))

    # Save the modified image
    image.save(output_path)

@st.cache_resource
def initialization_function():
    print('MADE IT')
    # Create a connection object.
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
    return conn, df

def main():

    conn , df = initialization_function()

    st.title("Brewmaster's Bargain Bin")

    name = st.text_input("Name your brew:")
    description = st.text_area("Describe your brew:")
    effect = st.text_area("What is your brew Effect:")

    if st.button("Submit"):
        if name in df.values:
            st.warning("Brew already exists!")
        elif name and description and effect:
            print(df.index)
            df.loc[len(df.index)] = [name, description, effect]
            df = conn.update(data=df)
            print(df.index)
            st.info('New Brew ADDED!', icon="🧙‍♀️")
        else:
            st.warning("Please enter ALL brew info")
        print(df)

    st.write("##")

    if st.button("PICK YOUR POISON"):
        add_text_to_image("potion_background.jpg", text, output_path, 40, 70)
        add_text_to_image("potion_background.jpg", text, output_path, 120, 70)
        st.image(output_path)
        # st.image("potion_background.jpg")


main()
