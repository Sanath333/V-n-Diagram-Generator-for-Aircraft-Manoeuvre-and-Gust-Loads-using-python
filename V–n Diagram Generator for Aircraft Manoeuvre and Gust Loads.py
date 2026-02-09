import numpy as np
import matplotlib.pyplot as plt

W = float(input("Enter aircraft weight (N): "))          
S = float(input("Enter wing area (m^2): "))             
c_bar = float(input("Enter mean aerodynamic chord: "))                 
n_limit_p = float(input("Enter positive limit load factor: ")) 
n_limit_n = float(input("Enter negetive limit load factor: "))    
CL_max_p = float(input("Enter CLmax(+): ")) 
CL_max_n = float(input("Enter CLmax(-): "))                    
CL_alpha = float(input("Enter CLalpha (per rad): "))
Vca = float(input("Enter Cruise Speed Vc (m/s): "))
Vda = float(input("Enter Dive Speed Vd (m/s): "))
Ude = float(input("Enter gust velocity Ude (m/s): "))   

rho = 1.225        
g = 9.81

Vd = np.linspace(0, Vda, 500) 
Vc = np.linspace(0, Vca, 500) 

n_manoeuvre_p = (0.5 * rho * Vd**2 * S * CL_max_p) / W
n_manoeuvre_p = np.minimum(n_manoeuvre_p, n_limit_p)
n_manoeuvre_n = (0.5 * rho * Vd**2 * S * CL_max_n) / W
n_manoeuvre_n = np.minimum(n_manoeuvre_n, n_limit_n)


mu = (2 * W) / (S* CL_alpha * c_bar)
K_g = (0.88 * mu) / (1+ mu)


delta_n_gust_vc = (rho * Vc * Ude * S * CL_alpha * K_g) / (2 * W)
n_gust_vc_p = 1 + delta_n_gust_vc
n_gust_vc_n = 1 - delta_n_gust_vc
Ude_d= Ude/2
delta_n_gust_vd = (rho * Vd * Ude_d * S * CL_alpha * K_g) / (2 * W)
n_gust_vd_p = 1 + delta_n_gust_vd
n_gust_vd_n = 1 - delta_n_gust_vd

V_s = np.sqrt((2 * W) / (rho * S * CL_max_p))
V_A = V_s * np.sqrt(n_limit_p)

plt.figure(figsize=(15,15))
plt.plot(Vd, n_manoeuvre_p, label="Manoeuvre", linewidth=2)
plt.plot(Vd, n_manoeuvre_n, label="Manoeuvre", linewidth=2)
plt.plot(Vc, n_gust_vc_p, label="Gust@Vc", linestyle="--", linewidth=2, color="Red")
plt.plot(Vc, n_gust_vc_n, label="Gust@Vc", linestyle="--", linewidth=2, color="Red")
plt.plot(Vd, n_gust_vd_p, label="Gust@Vd", linestyle="--", linewidth=2, color="Brown")
plt.plot(Vd, n_gust_vd_n, label="Gust@Vd", linestyle="--", linewidth=2, color="Brown")
plt.axvline(V_s, linestyle=":", label="Vs", color="Red")
plt.axvline(V_A, linestyle=":", label="Va", color="Green")
plt.axvline(Vca, linestyle=":", label="Vc" )
plt.axvline(Vda, linestyle=":", label="Vd" )
plt.xlabel("Speed (m/s)")
plt.ylabel("Load Factor (n)")
plt.title("V–n Diagram (Manoeuvre + Gust)")
plt.grid(True)
plt.legend()
plt.show()