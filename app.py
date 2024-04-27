import streamlit as st

# Function to get file category based on file extension
def get_category(file_extension):
    if file_extension in ["dxf", "dwg"]:
        return "CAD"
    elif file_extension in ["shp", "geojson", "kml", "kmz"]:
        return "GIS"
    elif file_extension in ["las", "laz"]:
        return "Point Cloud"
    elif file_extension == "3dtiles":
        return "3D Data"
    else:
        return "Unknown"

# Function to display file information
def display_file_info(file):
    file_name = file.name
    file_extension = file_name.split(".")[-1].lower()
    category = get_category(file_extension)
    if category == "Unknown":
        st.error("Unsupported file format.")
        return
    else:
        st.success(f"File uploaded: {file_name}")
        st.info(f"Category: {category}")
        st.info(f"File extension: {file_extension}")

# Başlık
st.title("Veri Gösterme Uygulaması")

# Dosya yükleme
uploaded_file = st.file_uploader("Lütfen bir dosya yükleyin", type=["dxf", "dwg", "shp", "geojson", "kml", "kmz", "las", "laz", "3dtiles"])

# Dosya bilgisi gösterme
if uploaded_file is not None:
    display_file_info(uploaded_file)
