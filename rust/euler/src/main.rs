extern crate ndarray;

use ndarray::prelude::*;


fn f(t: f64, y: Array<f64, Ix1>) -> Array<f64, Ix1> {
	let mu1 = 50.;  // prey
	let mu2 = 25.;  // predator
	return array![y[0] * (1. - y[1]/mu1),
	              -y[1] * (1. - y[0]/mu2)];
}

fn main() {
	let mut yn = array![100.,25.];
    println!("Hello, world!");
    println!("{:?}", f(10., yn));
    let mut data = Vec::new();
    let h = 0.01;
    let mut tn = 0.;

    for _ in 0..100 {
    	yn = yn + h * f(tn, yn);
		data.push((tn, yn));
    	tn = tn + h;
    }
}

