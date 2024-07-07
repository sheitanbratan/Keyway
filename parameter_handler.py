def parameter_handler() -> list:
    z_start_point = float(input('Enter Z axis start point: '))
    x_start_point = float(input('Enter X axis start point: '))
    z_finish_point = float(input('Enter Z axis finish point: '))
    x_finish_point = float(input('Enter X axis finish point: '))
    depth_of_cut = float(input('Enter depth of cut: '))
    feed = float(input('Enter feed: '))

    next_cut_value = x_start_point

    return [
        z_start_point, x_start_point,
        z_finish_point, x_finish_point,
        depth_of_cut, feed, next_cut_value
    ]