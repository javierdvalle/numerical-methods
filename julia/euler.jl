using PyPlot

function euler(t, yn, h, f)
    return yn + h*f(t, yn)
end

function main()

	t0, y0 = 0, 0
	tn, yn = t0, y0
	h = 0.1
	t_last = 10
	T, Y = [], []

	f(t, y) = sin(t)

	t = 0
	for i in 1:trunc(Int, (t_last-t0)/h)
	    yn = euler(tn, yn, h, f)
	    append!(T, tn)
	    append!(Y, yn)
	    tn = tn + h
	end

	plot(T, Y)
	show()
end

main()