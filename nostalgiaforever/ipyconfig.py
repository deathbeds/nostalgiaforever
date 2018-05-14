from traitlets.config import get_config
c = get_config()
# c.InteractiveShellApp.extensions.insert(0, ['pidgin.markdown', 'pidgin.conventions'])
c.InteractiveShellApp.extensions = [
    'importnb.utils.ipython', 'pidgin.markdown', 'pidgin.conventions'
]
