import hexchat


__module_name__ = 'ZNC clearbuffer'
__module_author__ = 'fladd'
__module_version__ = '1.0'
__module_description__ = 'Clear the ZNC buffer on window close'


def clearbuffer(*args):
    channel = hexchat.get_info('channel')
    if not channel.startswith("*"):
        for chan in hexchat.get_list('channels'):
            if chan.type == 1 and chan.id == hexchat.get_prefs('id'):
                chan.context.command("msg *status clearbuffer {0}".format(
                    channel))

hexchat.hook_print('Close Context', clearbuffer)
