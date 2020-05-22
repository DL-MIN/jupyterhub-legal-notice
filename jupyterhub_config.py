from jupyterhub.handlers.base import BaseHandler

class LegalNoticeHandler(BaseHandler):
    async def get(self):
        html = self.render_template('legal-notice.html')
        self.finish(html)

class PrivacyPolicyHandler(BaseHandler):
    async def get(self):
        html = self.render_template('privacy-policy.html')
        self.finish(html)

c.JupyterHub.extra_handlers = [(r'/legal-notice', LegalNoticeHandler), (r'/privacy-policy', PrivacyPolicyHandler)]
c.JupyterHub.template_paths = ['/var/web/jupyterhub']
