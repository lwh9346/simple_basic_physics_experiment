import simple_exp as se

x, y = se.load_csv_XY("example_data.csv")
se.plot_linear_fit_result(x, y, file_name="example_linear.png")
se.plot_curve(x, y, file_name="example_curve.png")
