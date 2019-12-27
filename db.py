from resur import q


def get_question(ticket_number, question_number):

    question = q.questions[ticket_number][question_number]
    return question


def get_write_answer(ticket_number, question_number):

    write_answer = q.answers[ticket_number][question_number]
    return write_answer


def get_comment(ticket_number, question_number):

    comment = q.comments[ticket_number][question_number]
    return comment


def get_picture(ticket_number, question_number):

    picture = q.pictures[ticket_number][question_number]
    return picture


def get_number_of_choices(ticket_number, question_number):

    number_of_choices = q.choices[ticket_number][question_number]
    return number_of_choices