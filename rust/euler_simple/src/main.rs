use plotlib::repr::Plot;
use plotlib::view::ContinuousView;
use plotlib::page::Page;
use plotlib::style::{PointMarker, PointStyle};

mod euler;


fn f(t: f64, _y: f64) -> f64 {
	t.sin()
}


fn plot_data(data: Vec<(f64, f64)>) {
	let v = ContinuousView::new()
        .add(Plot::new(data).point_style(
		        PointStyle::new()
		            .marker(PointMarker::Circle)
		            .colour("#DD3355"),
		    )
        )
        // .x_range(0., 10.)
        // .y_range(-1., 10.)
        .x_label("t")
        .y_label("y");

    Page::single(&v).save("plot.svg").unwrap();
    println!("Plot saved to file: plot.svg");

    println!("{}", Page::single(&v).dimensions(100, 20).to_text().unwrap());
}


fn main() {

	let t0 = 0.0;
	let y0 = 0.0;
    let mut tn = t0; 
    let mut yn = y0;
    let h = 0.001;
    let t_end = 10.0;
    let limit = ((t_end-t0)/h) as i64;
    let mut data = Vec::new();
    let method = euler::euler;

    for _n in 0..limit {
    	yn = method(tn, yn, h, f);
    	data.push((tn, yn));
    	tn = tn + h;
    	// println!("{:?} - {:?}", tn, yn);
    }

    println!("{:?} points", data.len());

    plot_data(data);
}
