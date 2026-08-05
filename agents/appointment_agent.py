def appointment_agent(state):

    question = state["user_question"].lower()

    # Book appointment
    if any(word in question for word in [
        "book",
        "appointment",
        "schedule",
        "reserve"
    ]):
        return {
            "answer": "To book an appointment, use the POST /appointments/book API."
        }

    # Cancel appointment
    if any(word in question for word in [
        "cancel",
        "delete",
        "remove"
    ]):
        return {
            "answer": "To cancel an appointment, use the DELETE /appointments/cancel/{appointment_id} API."
        }

    # Reschedule appointment
    if any(word in question for word in [
        "reschedule",
        "change",
        "modify",
        "update"
    ]):
        return {
            "answer": "To reschedule an appointment, use the PUT /appointments/reschedule/{appointment_id} API."
        }

    # View appointments
    if any(word in question for word in [
        "view",
        "list",
        "show",
        "appointments"
    ]):
        return {
            "answer": "To view appointments, use the GET /appointments/view API."
        }

    return {
        "answer": (
            "I can help you with appointments. "
            "You can book, cancel, reschedule, or view appointments."
        )
    }