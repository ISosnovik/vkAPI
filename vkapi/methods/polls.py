# Polls methods
from ..api import call, parse_response


def addVote(owner_id=None, poll_id=None, answer_id=None, is_board=None):
    """
    Adds the current user's vote to the selected answer
    in the poll.
    https://vk.com/dev/polls.addVote
    """
    params = {
        'owner_id': owner_id,
        'poll_id': poll_id,
        'answer_id': answer_id,
        'is_board': is_board
    }
    result = call('polls.addVote', **params)
    return parse_response(result)


def create(question=None, is_anonymous=None, owner_id=None, add_answers=None):
    """
    Creates polls that can be attached to the users' or
    communities' posts.
    https://vk.com/dev/polls.create
    """
    params = {
        'question': question,
        'is_anonymous': is_anonymous,
        'owner_id': owner_id,
        'add_answers': add_answers
    }
    result = call('polls.create', **params)
    return parse_response(result)


def deleteVote(owner_id=None, poll_id=None, answer_id=None, is_board=None):
    """
    Deletes the current user's vote from the selected answer
    in the poll.
    https://vk.com/dev/polls.deleteVote
    """
    params = {
        'owner_id': owner_id,
        'poll_id': poll_id,
        'answer_id': answer_id,
        'is_board': is_board
    }
    result = call('polls.deleteVote', **params)
    return parse_response(result)


def edit(owner_id=None, poll_id=None, question=None, add_answers=None, edit_answers=None,\
         delete_answers=None):
    """
    Edits created polls
    https://vk.com/dev/polls.edit
    """
    params = {
        'owner_id': owner_id,
        'poll_id': poll_id,
        'question': question,
        'add_answers': add_answers,
        'edit_answers': edit_answers,
        'delete_answers': delete_answers
    }
    result = call('polls.edit', **params)
    return parse_response(result)


def getById(owner_id=None, is_board=None, poll_id=None):
    """
    Returns detailed information about a poll by its ID.
    https://vk.com/dev/polls.getById
    """
    params = {
        'owner_id': owner_id,
        'is_board': is_board,
        'poll_id': poll_id
    }
    result = call('polls.getById', **params)
    return parse_response(result)


def getVoters(owner_id=None, poll_id=None, answer_ids=None, is_board=None,\
              friends_only=None, offset=None, count=None, fields=None, name_case=None):
    """
    Returns a list of IDs of users who selected specific
    answers in the poll.
    https://vk.com/dev/polls.getVoters
    """
    params = {
        'owner_id': owner_id,
        'poll_id': poll_id,
        'answer_ids': answer_ids,
        'is_board': is_board,
        'friends_only': friends_only,
        'offset': offset,
        'count': count,
        'fields': fields,
        'name_case': name_case
    }
    result = call('polls.getVoters', **params)
    return parse_response(result)


