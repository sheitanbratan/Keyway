from program_header import header
from program_footer import footer
from parameter_handler import parameter_handler


# Main func
def generate_code(
        z_start_point, x_start_point,
        z_finish_point, x_finish_point,
        depth_of_cut, feed, next_cut_value
) -> None:

    """
    Generates and writes G-code to .NC file

    :param z_start_point: Start point for Z axis
    :param x_start_point: Start point for X axis
    :param z_finish_point: Finish point for Z axis
    :param x_finish_point: Finish point for X axis
    :param depth_of_cut: Depth of cut
    :param feed: Feed
    :param next_cut_value: X axis value for next cutting move
    :return: None
    """

    file.write("(tiktok.com/@sheitanbratan)\n")
    file.write(f"G00 C{c_axis_value}\n")  # start point of the rotating axis
    file.write(f"G00 Z{z_start_point}\n")    # go to Z start point
    file.write(f"G00 X{x_start_point}\n")    # go to X start point
    file.write("M8 ;\n")    # Coolant On
    while next_cut_value < x_finish_point:
        next_cut_value += depth_of_cut
        next_cut_value = round(next_cut_value, 3)
        if next_cut_value > x_finish_point:
            next_cut_value = x_finish_point

        file.write(f"X{next_cut_value}\n")
        file.write(f"G01 Z{z_finish_point} F{feed}\n")
        file.write(f"G00 X{x_start_point}\n")
        file.write(f"Z{z_start_point}\n")
    file.write("M9 ;\n")
    file.write(f"M01 ;\n")  # Optional stop


with open("G-code.nc", "w") as file:
    header = header()
    footer = footer()
    for header_line in header:
        file.write(header_line)

    # Program logic:
    waiting_for_choosing = True
    while waiting_for_choosing:
        print(f'Choose mode:\n[1] Hand mode\n[2] From file\n[3] Exit')
        mode_choosing = input('>>: ')
        if mode_choosing == '1':

            c_axis_value = 0.0   # default parameter for C axis
            print('Default C-axis value is 0. Do you want to change?')
            confirm = input('[Y]/[N]?').upper()
            if confirm == 'Y':
                c_axis_value = float(input('Enter C axis start point: '))
            else:
                pass

            params = parameter_handler()
            generate_code(
                z_start_point=params[0], x_start_point=params[1],
                z_finish_point=params[2], x_finish_point=params[3],
                depth_of_cut=params[4], feed=params[5], next_cut_value=params[6]
            )
            print(f'Do you want to change C-axis value? C-axis value is {c_axis_value} now')
            confirm = input('[Y]/[N]?').upper()
            while confirm == 'Y':
                c_axis_value = float(input('Enter new C axis value: '))
                generate_code(
                    z_start_point=params[0], x_start_point=params[1],
                    z_finish_point=params[2], x_finish_point=params[3],
                    depth_of_cut=params[4], feed=params[5], next_cut_value=params[6]
                )
                print(f'Do you want to change C-axis value? C-axis value is {c_axis_value} now')
                confirm = input('Y/N?').upper()
            else:
                for footer_line in footer:
                    file.write(footer_line)

        elif mode_choosing == '2':
            print('Enter a path to file with list of angles')
            Path = input('Path to file: ')
            print('Now enter parameters')
            params = parameter_handler()
            with open(Path, 'r') as diff:
                for line in diff.readlines():
                    if len(line) > 1:
                        c_axis_value = float(line)
                        generate_code(
                            z_start_point=params[0], x_start_point=params[1],
                            z_finish_point=params[2], x_finish_point=params[3],
                            depth_of_cut=params[4], feed=params[5], next_cut_value=params[6]
                        )
            for footer_line in footer:
                file.write(footer_line)
        elif mode_choosing == '3':
            waiting_for_choosing = False
        else:
            print('Wrong choice. Try again')
            continue
