import math

DISTANCE_TO_PIVOT = 1
DISTANCE_TO_SL = 6

# Constants for gate
GATE_RADIUS, MIN_ELEV = (1804.238, 7.987)

def plot_sample(ax, sample,
                DISTANCE_TO_SL=DISTANCE_TO_SL,
                DISTANCE_TO_PIVOT=DISTANCE_TO_PIVOT,
               GATE_RADIUS=GATE_RADIUS,
               MIN_ELEV=MIN_ELEV):
    """# Plotting Water Surface profile"""
    
    # Horizontal distance from gate hinge to gate tip
    L = math.cos(math.radians(sample.G1_ANGLE))*(GATE_RADIUS/1000)
    
    # Shift datum for levels
    datum = MIN_ELEV
    
    g1_el = sample.G1_ELEVATION - MIN_ELEV
    usl = sample.USL_VAL-MIN_ELEV
    d = sample.G1_ELEVATION - MIN_ELEV + sample.Cc*sample.hu
    dsl = sample.DSL_VAL-MIN_ELEV
    sl = sample.SL_DEPTH_COR-MIN_ELEV
    
    # Plot Gate Angle
    gate_x = [DISTANCE_TO_PIVOT, DISTANCE_TO_PIVOT+L]
    gate_y = [0, g1_el]
    
    ax.plot(gate_x, gate_y, color='k', label='Gate')

    ws_x = [0.5, L+DISTANCE_TO_PIVOT, (GATE_RADIUS/1000)+DISTANCE_TO_PIVOT+0.5, DISTANCE_TO_SL]
    ws_y = [usl, d, dsl, sl]

    ax.plot(ws_x, ws_y, marker='o', label='WS', color='blue')
    
    #ax.legend()
    
    # add dashed lines for each level/ elevation
    names = ['USL Level', 'Depth at Gate Tip', 'Gate DSL Level', 'Pool DSL Level']
    buffer = 0.02
    for i in range(0, len(names)):

        #ax.plot([0, ws_x[i]], [ws_y[i], ws_y[i]], ls='--', color='grey')
        
        ax.text(ws_x[i]+buffer, ws_y[i]+buffer, names[i])

    ax.plot(DISTANCE_TO_SL+1, 0)
    
    ax.set(xlabel='Distance [m]', ylabel='Height Above Gate Hinge [m]')
    return ax
# plto curved line through points
#from scipy.interpolate import make_interp_spline, BSpline

# 300 represents number of points to make between T.min and T.max
#xnew = np.linspace(min(ws_x), max(ws_x), 300)  

#spl = make_interp_spline(ws_x, ws_y, k=2)  # type: BSpline
#ws_smooth = spl(xnew)

#plt.plot(xnew, ws_smooth)


# plt.plot(0, sample.USL_VAL - min_elev, label='USL', marker='o')
# plt.plot(L,
#          sample.G1_ELEVATION - min_elev + sample.Cc*sample.hu, label='h' , marker='o')

# plt.plot((gate_radius/1000), sample.DSL_VAL - min_elev, label='DSL', marker='o')

# plt.plot(5, sample.SL_DEPTH_COR - min_elev, label='SL', marker='o')

# plt.legend()
