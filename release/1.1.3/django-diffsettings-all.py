#!/usr/bin/env python
# Based on Django 1.5 diffsettings
# https://github.com/django/django/blob/1.5/django/core/management/commands/diffsettings.py
import sys


def module_to_dict(module, omittable=lambda k: k.startswith('_')):
    "Converts a module namespace to a Python dictionary. Used by get_settings_diff."
    return dict([(k, repr(v)) for k, v in module.__dict__.items() if not omittable(k)])


def main():
    # Inspired by Postfix's "postconf -n".
    from django.conf import settings, global_settings

    # Because settings are imported lazily, we need to explicitly load them.
    settings._setup()

    user_settings = module_to_dict(settings._wrapped)
    default_settings = module_to_dict(global_settings)

    output = []
    for key in sorted(user_settings.keys()):
        if key not in default_settings:
            output.append("%s = %s  ###" % (key, user_settings[key]))
        elif user_settings[key] != default_settings[key]:
            output.append("%s = %s" % (key, user_settings[key]))
        else:
            output.append("### %s = %s" % (key, user_settings[key]))
    return '\n'.join(output)


if __name__ == '__main__':
    sys.stdout.write(main() + '\n')
