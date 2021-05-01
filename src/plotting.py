# Plotting Water Surface profile
sample = data.iloc[-1]

d_to_pivot = 0.5
d_to_sl = 5

L = math.cos(math.radians(sample.G1_ANGLE))*(gate_radius/1000)
# plt.plot(L,
#          sample.G1_ELEVATION - min_elev, label='Gate El' , marker='x')
# plt.plot(d_to_pivot, 0, label='Gate Pivot' , marker='x')

gate_x = [d_to_pivot, d_to_pivot+L]
gate_y = [0, sample.G1_ELEVATION - min_elev]
plt.plot(gate_x, gate_y, color='k', label='Gate')

ws_x = [0, L+d_to_pivot, (gate_radius/1000)+d_to_pivot+0.5, d_to_sl]
ws_y = [sample.USL_VAL-min_elev,
        sample.G1_ELEVATION - min_elev + sample.Cc*sample.hu,
       sample.DSL_VAL-min_elev,
       sample.SL_DEPTH_COR-min_elev]

plt.scatter(ws_x, ws_y, marker='o', label='WS')

from scipy.interpolate import make_interp_spline, BSpline

# 300 represents number of points to make between T.min and T.max
xnew = np.linspace(min(ws_x), max(ws_x), 300)  

spl = make_interp_spline(ws_x, ws_y, k=2)  # type: BSpline
ws_smooth = spl(xnew)

plt.plot(xnew, ws_smooth)

# plt.plot(0, sample.USL_VAL - min_elev, label='USL', marker='o')
# plt.plot(L,
#          sample.G1_ELEVATION - min_elev + sample.Cc*sample.hu, label='h' , marker='o')

# plt.plot((gate_radius/1000), sample.DSL_VAL - min_elev, label='DSL', marker='o')

# plt.plot(5, sample.SL_DEPTH_COR - min_elev, label='SL', marker='o')

# plt.legend()
