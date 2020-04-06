use plotlib::repr::Plot;
use plotlib::view::ContinuousView;
use plotlib::page::Page;
use plotlib::style::{PointMarker, PointStyle};

fn f(t: f64, _y: f64) -> f64 {
	t.sin()
}

fn euler(tn: f64, yn: f64, h: f64, f: fn(f64, f64) -> f64) -> f64 {
	yn + h*f(tn, yn)
}


fn main() {

	let t0 = 0.0;
	let y0 = 0.0;
    let mut tn = t0; 
    let mut yn = y0;
    let h = 0.001;
    let t_last = 10.0;
    let mut data = Vec::new();
    let limit = ((t_last-t0)/h) as i64;

    for _i in 0..limit {
    	yn = euler(tn, yn, h, f);
    	data.push((tn, yn));
    	tn = tn + h;
    	// println!("{:?} - {:?}", tn, yn);
    }

    println!("{:?} points", data.len());

    let v = ContinuousView::new()
        .add(Plot::new(data).point_style(
		        PointStyle::new()
		            .marker(PointMarker::Circle)
		            .colour("#DD3355"),
		    )
        )
        // .x_range(0., 10.)
        // .y_range(-1., 6.)
        .x_label("Some varying variable")
        .y_label("The response of something");

    Page::single(&v).save("plot.svg").unwrap();
    println!("Plot saved to file: plot.svg");
}
