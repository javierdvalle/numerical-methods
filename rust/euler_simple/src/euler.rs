
pub fn euler(tn: f64, yn: f64, h: f64, f: fn(f64, f64) -> f64) -> f64 {
	yn + h*f(tn, yn)
}
