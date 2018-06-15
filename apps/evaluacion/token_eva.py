
from django.contrib.auth.tokens import PasswordResetTokenGenerator

#devido a que todas la clases de token son las mismas se usa un solo generador de tokens
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        # aqui crear en cero todo
        # Ensure results are consistent across DB backends
        #login_timestamp = '' if user.last_login is None else user.last_login.replace(microsecond=0, tzinfo=None)
        return str(user.pk) + str(user.evaluacion) + str(user.numero_ran) + str(user.usado) + str(user.creacion)

evaluacion_token_generator = TokenGenerator()

"""
class TokenGenerator:

    #Strategy object used to generate and check tokens for the password
    #reset mechanism.

    #key_salt = "django.contrib.auth.tokens.PasswordResetTokenGenerator"
    key_salt = "apps.evaluacion.token_eva.TokenGenerator"
    secret = settings.SECRET_KEY

    def make_token(self, user):
        #Return a token that can be used once to do a password reset
        #for the given user.
        return self._make_token_with_timestamp(user, self._num_days(self._today()))

    def check_token(self, user, token):
        
        #Check that a password reset token is correct for a given user.
        
        if not (user and token):
            return False
        # Parse the token
        try:
            ts_b36, hash = token.split("-")
        except ValueError:
            return False

        try:
            ts = base36_to_int(ts_b36)
        except ValueError:
            return False

        # Check that the timestamp/uid has not been tampered with
        if not constant_time_compare(self._make_token_with_timestamp(user, ts), token):
            return False

        # Check the timestamp is within limit
        if (self._num_days(self._today()) - ts) > settings.PASSWORD_RESET_TIMEOUT_DAYS:
            return False

        return True

    def _make_token_with_timestamp(self, user, timestamp):
        # timestamp is number of days since 2001-1-1.  Converted to
        # base 36, this gives us a 3 digit string until about 2121
        ts_b36 = int_to_base36(timestamp)

        # By hashing on the internal state of the user and using state
        # that is sure to change (the password salt will change as soon as
        # the password is set, at least for current Django auth, and
        # last_login will also change), we produce a hash that will be
        # invalid as soon as it is used.
        # We limit the hash to 20 chars to keep URL short

        hash = salted_hmac(
            self.key_salt,
            self._make_hash_value(user, timestamp),
            secret=self.secret,
        ).hexdigest()[::2]
        return "%s-%s" % (ts_b36, hash)

    def _make_hash_value(self, user, timestamp):
        # aqui crear en cero todo
        # Ensure results are consistent across DB backends
        #login_timestamp = '' if user.last_login is None else user.last_login.replace(microsecond=0, tzinfo=None)
        return str(user.pk) + str(user.evaluacion) + str(user.numero_ran) + str(user.usado) + str(user.creacion)

    def _num_days(self, dt):
        return (dt - date(2001, 1, 1)).days

    def _today(self):
        # Used for mocking in tests
        return date.today()


evaluacion_token_generator = TokenGenerator()
"""