from visualizations.mapa import figura_mapa

if __name__ == '__main__':
    fig = figura_mapa(2026)
    print('Tipo:', type(fig))
    d = fig.to_dict()
    print('Keys:', list(d.keys()))
    print('Traces:', len(fig.data))
    for i,t in enumerate(fig.data[:5]):
        lat = getattr(t, 'lat', None)
        lon = getattr(t, 'lon', None)
        print(i, getattr(t, 'type', None), getattr(t, 'name', None), 'lat_points=', len(lat) if lat is not None else 0)
