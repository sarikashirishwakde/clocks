def clockangle(request):
    request_json = request.get_json()
    if request.args and 'input_time' in request.args:
        input_time = request.args.get('input_time')
    elif request_json and 'input_time' in request_json:
        input_time = request_json['input_time']
    else:
        return f'Try one more time'
    try:
        data = input_time.split(':')
        hour = int(data[0])
        minute = int(data[1])
        if(hour < 0 or minute <0 or hour > 12 or minute >60):
            raise Exception("Wrong Input!!")
        angle_hour=(360/12)*(hour+(minute/60))
        angle_minute=(360/60)*minute
        angle=float(abs(angle_hour-angle_minute))
        print("The time is {}:{} \n".format(hour,minute))
        print("Angle is {} degree \n".format(angle))
        return "Angle is {} degree \n".format(angle)
    except Exception:
        print("Please Enter valid Hour & Minute")
