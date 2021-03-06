# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:57:29 2016

@author: studi
"""

from numpy import *
import matplotlib.pyplot as plt

def get_h_r(l_e, h_m, phi):
    #Kosinussatz
    return sqrt(l_e **2 + h_m**2 - 2*l_e*h_m * cos(phi))
    
def get_alpha(l_e, phi, h_r):
    # Sinussatz
    return arcsin(l_e * sin(phi)/h_r)
    
def get_beta(alpha, psi):
    # Analysis
    return pi - alpha - psi

def get_h(psi, h_b, beta):
    # Sinussatz
    return sin(psi) * h_b / sin(beta)

def get_gamma(lr,hr):
    return arcsin(lr/hr)

def get_third(beta,gamma):
    return pi-beta-gamma

def get_eps(beta):
    return pi - beta

def get_b_bottom(h, beta, gamma):
    # Sinussatz
    delta=get_third(beta,gamma)
    return (sin(gamma)/sin(delta))*h

def get_b_top(h,beta,gamma):
    eps = get_eps(beta)
    zeta = get_third(gamma,eps)
    return (sin(gamma)/sin(zeta))*h
    
def get_b(h,beta,gamma):
    return get_b_top(h,beta,gamma) + get_b_bottom(h,beta,gamma)
    
def make_plot(h_b, h_m, l_e, l_r, phi, h_r, h, b, b_top, b_bottom, psi, alpha, beta, gamma):
    plt.clf()
    plt.close() 
    plt.axis((-0.5,h_b+0.5,-1.5*b,1.5*b))
    pointpsix, pointpsiy = plot_line(0,0,get_rad(0),h_b, name="hb")
    topx,topy = plot_line(pointpsix,pointpsiy,pi-psi,1.3*b, plot=False)
    plot_line(topx,topy,2*pi-psi,2.6*b)
    pointphix,pointphiy = plot_line(0,0,get_rad(0),h_m, name="hm")
    #plot_line(h_m,0,phi,l_e)
    pointbx, pointby = plot_line(0,0,alpha,h, name="h")
    pointrx, pointry = plot_line(0,0,alpha,h_r, name="hr")
    btopx,btopy = plot_line(pointbx,pointby,pi-psi,b_top, plot=False)
    plot_line(btopx,btopy,2*pi-psi,b, name="b")
    bbottomx,bbottomy = plot_line(pointbx,pointby,2*pi-psi,b_bottom, plot=False)
    plt.plot((0,bbottomx),(0,bbottomy),'k-.')
    plt.plot((0,btopx),(0,btopy),'k-.')
    circlele=plt.Circle((pointphix,pointphiy),l_e,color='k',linestyle='dashed',fill=False)
    circler=plt.Circle((pointrx,pointry),l_r,color='k',fill=False)
    fig = plt.gcf()
    ax = plt.gca()
    fig.gca().add_artist(circlele)
    fig.gca().add_artist(circler)
    plt.axis('equal')
    plt.legend()
    plt.show()

def plot_line(pointx, pointy, angle, distance, plot=True, name=None):
    x = cos(angle)*distance+pointx
    y = sin(angle)*distance+pointy
    if plot:
        plt.plot((pointx,x),(pointy,y),'-', label=name)
    return x,y

def get_rad(angle):
    return angle/180*pi
    
def main(
    l_e = 1,
    l_r = 0.5,
    h_m = 2,
    phi_0 = get_rad(180),
    delta_phi = 0,
    psi = pi/2,
    h_b = 4):
    phi = delta_phi + phi_0
    h_r = get_h_r(l_e, h_m, phi)
    alpha = get_alpha(l_e, phi, h_r)
    beta = get_beta(alpha, psi)
    h = get_h(psi, h_b, beta)
    gamma = get_gamma(l_r, h_r)
    b_bottom = get_b_bottom(h,beta,gamma)
    b_top = get_b_top(h,beta,gamma)
    b = get_b(h, beta, gamma)
    print(b)
    make_plot(h_b, h_m, l_e, l_r, phi, h_r, h, b, b_top, b_bottom, psi, alpha, beta, gamma)
    
    

if __name__ == "__main__":
    main(l_e=2, l_r=1, h_m=3.5, phi_0=get_rad(135), delta_phi=get_rad(0), psi=get_rad(75), h_b=8)
    main(l_e=2, l_r=1, h_m=3.5, phi_0=get_rad(135), delta_phi=get_rad(45), psi=get_rad(75), h_b=8) 
    main(l_e=2, l_r=1, h_m=3.5, phi_0=get_rad(135), delta_phi=get_rad(90), psi=get_rad(75), h_b=8)
    main(l_e=2, l_r=1, h_m=3.5, phi_0=get_rad(135), delta_phi=get_rad(135), psi=get_rad(75), h_b=8)
    main(l_e=2, l_r=1, h_m=3.5, phi_0=get_rad(135), delta_phi=get_rad(180), psi=get_rad(75), h_b=8)
    main(l_e=2, l_r=1, h_m=3.5, phi_0=get_rad(135), delta_phi=get_rad(225), psi=get_rad(75), h_b=8)
    main(l_e=2, l_r=1, h_m=3.5, phi_0=get_rad(135), delta_phi=get_rad(270), psi=get_rad(75), h_b=8)
    main(l_e=2, l_r=1, h_m=3.5, phi_0=get_rad(135), delta_phi=get_rad(315), psi=get_rad(75), h_b=8)
    quit()
