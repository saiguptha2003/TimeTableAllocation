import random

def define_problem(classroomCount,sectionCount,slotCount):
    sectionCount=int(sectionCount)
    sections = ['Section'+str(i) for i in range(1,sectionCount+1)]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    time_slots = ['Slot'+str(i) for i in range(1,slotCount+1)]
    classrooms=['Classroom'+str(i) for i in range(1,classroomCount+1)]
    schedule = {(section, day, time): None for section in sections for day in days for time in time_slots}
    # print(schedule)
    return schedule, sections, days, time_slots, classrooms

def can_schedule(schedule, section, day, time, classroom, classroom_counts,sectionCount):
    if (section, day, time) in schedule.keys() and schedule[(section, day, time)] is not None:
        return False
    
    if classroom_counts[classroom] >= len(schedule) // sectionCount:
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
        if can_schedule(schedule, section, day, time, classroom, classroom_counts,len(sections)):
            schedule[(section, day, time)] = classroom
            classroom_counts[classroom] += 1

            if schedule_class(schedule, sections, days, time_slots, classrooms, class_index + 1, classroom_counts):
                return True

            schedule[(section, day, time)] = None
            classroom_counts[classroom] -= 1

    return False


def findpattern(classCount,sectionCount,slotCount):
    schedule, sections, days, time_slots, classrooms = define_problem(classCount,sectionCount,slotCount)
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
        print(timetable)
        return (timetable,time_slots)
    else:
        print("No solution found")
        return [False, False]