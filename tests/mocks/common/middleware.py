def before_all(*args, **kwargs):
    before_all.called = True


def after_all(*args, **kwargs):
    after_all.called = True


def when_auth_required(*args, **kwargs):
    when_auth_required.called = True


def on_error(*args, **kwargs):
    on_error.called = True


def on_timeout(*args, **kwargs):
    on_timeout.called = True


def bad_on_error(*args, **kwargs):
    bad_on_error.called = True
    raise Exception('YOU DUN GOOFED!')
