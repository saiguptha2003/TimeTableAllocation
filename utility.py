import random

def define_problem():
    sections = ["Section1", "Section2", "Section3", "Section4", "Section5"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    time_slots = ["9AM-11AM", "12PM-2PM", "3PM-5PM"]
    schedule = {(section, day, time): None for section in sections for day in days for time in time_slots}
    return schedule, sections, days, time_slots

def can_schedule(schedule, section, day, time, classroom, classroom_counts):
    for existing_section, existing_day, existing_time in schedule.keys():
        if existing_day == day and existing_time == time and schedule[(existing_section, existing_day, existing_time)] == classroom:
            return False
    if classroom_counts[classroom] >= len(schedule) // len(classroom_counts):
        return False
    return True

def schedule_class(schedule, sections, days, time_slots, classrooms, class_index, classroom_counts):
    unscheduled_slots = len([slot for slot in schedule.values() if slot is None])
    available_classrooms = len(classrooms)*len(days)*len(time_slots) - sum(classroom_counts.values())
    
    if unscheduled_slots > available_classrooms:
        return False

    if class_index == len(sections) * len(days) * len(time_slots):
        return True
    section = sections[class_index // (len(days) * len(time_slots)) % len(sections)]
    day = days[class_index // len(time_slots) % len(days)]
    time = time_slots[class_index % len(time_slots)]

    random.shuffle(classrooms)

    for classroom in classrooms:
        if can_schedule(schedule, section, day, time, classroom, classroom_counts):
            schedule[(section, day, time)] = classroom
            classroom_counts[classroom] += 1

            if schedule_class(schedule, sections, days, time_slots, classrooms, class_index + 1, classroom_counts):
                return True

            schedule[(section, day, time)] = None
            classroom_counts[classroom] -= 1

    return False


def findpattern():
    classrooms = ["Classroom1", "Classroom2", "Classroom3", "Classroom4","Classroom5"]
    schedule, sections, days, time_slots = define_problem()
    classroom_counts = {classroom: 0 for classroom in classrooms}

    if schedule_class(schedule, sections, days, time_slots, classrooms, 0, classroom_counts):
        timetable=[]
        for section in sections:
            temptable=[]
            
            for day in days:
                row=[day]
                for slot in time_slots:
                    row.append(schedule[(section, day, slot)])
                temptable.append(row)
            timetable.append(temptable)
        time_slots=['day/time']+time_slots
        return (timetable,time_slots)
    else:
        return None