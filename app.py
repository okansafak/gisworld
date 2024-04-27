import streamlit as st
from streamlit.components.v1 import html

def openlayers_map(html_code):
    """
    OpenLayers haritasını göstermek için HTML kodunu içeren bir fonksiyon.
    """
    html_code_with_width = f'<div style="width: 100%; height: 500px;">{html_code}</div>'
    html(html_code_with_width)

def main():
    st.title("OpenLayers Harita Uygulaması")

    # OpenLayers haritası için gerekli JavaScript kodu
    openlayers_html = """
    <div id="map" class="map"></div>
    <script>
        import Map from 'ol/Map.js';
        import View from 'ol/View.js';
        import TileLayer from 'ol/layer/Tile.js';
        import OSM from 'ol/source/OSM.js';

        var map = new Map({
            layers: [
                new TileLayer({
                    source: new OSM()
                })
            ],
            target: 'map',
            view: new View({
                center: [0, 0],
                zoom: 2
            })
        });
    </script>
    """

    # OpenLayers haritasını Streamlit üzerinde göster
    openlayers_map(openlayers_html)

if __name__ == "__main__":
    main()
