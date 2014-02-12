import os.path
from tori.db.entity import entity
from tori.db.mapper import link, AssociationType as t, CascadingType as c

__triggering_script_template = """
#!/usr/bin/env bash

# Trigger the automation job via web API
curl -X POST\
    -H 'Content-Type: application/json'\
    -H 'X-Git-Listener: {git_listener_id}'\
    -d '{"automation": "{automation_id}"}'\
    {api_url}
;

# End of procedure
""".strip()

@link(
    target      = 'cis.model.Automation',
    mapped_by   = 'automation',
    association = t.MANY_TO_ONE
)
@entity
class GitListener(object):
    def __init__(self, hook_event, source, automation, api_url):
        self.hook_event = hook_event
        self.source     = source
        self.automation = automation
        self.api_url    = api_url
        self.__triggering_script_content = None

    def active(self):
        script_path = self.script_path()

        if not os.path.exists(script_path):
            return False

        existed_hook_script = None

        with open(script_path, 'r') as f:
            existed_hook_script = f.read()

        return existed_hook_script == self.script_content()

    def script_path(self):
        return os.path.abspath(os.path.join(self.source, 'hook', self.hook_event))

    def script_content(self):
        global __triggering_script_template

        if not self.__script_content:
            self.__script_content = __triggering_script_template.format(
                git_listener_id = self.id,
                automation_id   = self.automation.id,
                api_url         = self.api_url
            )

        return self.__script_content

    def activate(self):
        if self.active():
            return

        script_path = self.script_path()

        with open(script_path, 'w') as f:
            f.write(self.script())

    def deactivate(self):
        if not self.active():
            return

        script_path = self.script_path()

        if not os.path.exists(script_path):
            os.unlink(script_path)