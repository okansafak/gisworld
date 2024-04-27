import streamlit as st

def main():
    st.title("Okullar Haritası")

    # OpenLayers harita kodu
    openlayers_html = """
    <div id="map" style="width: 100%; height: 500px;"></div>
    <script src="https://cdn.jsdelivr.net/npm/ol@6.5.0/dist/ol.js"></script>
    <script>
        var map = new ol.Map({
            target: 'map',
            layers: [
                new ol.layer.Tile({
                    source: new ol.source.OSM()
                }),
                new ol.layer.Vector({
                    source: new ol.source.Vector({
                        url: 'okullar.geojson',
                        format: new ol.format.GeoJSON()
                    })
                })
            ],
            view: new ol.View({
                center: ol.proj.fromLonLat([35.447345028, 37.452493555]),
                zoom: 10
            })
        });
    </script>
    """

    # OpenLayers haritasını göster
    st.markdown(openlayers_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
