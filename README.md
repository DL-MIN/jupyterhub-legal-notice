# Jupyter Legal Notice

To display a legal notice and the privacy policy in the menu bar, handlers can be added in the JupyterHub configuration.

![Screenshot](/screenshot.png)


## Install

1. Replace the dummy texts in the files `web/legal-notice.html` and `web/privacy-policy.html`
2. Copy all files of `web/` directory to your accessible webserver
3. Add additional configurations of `jupyterhub_config.py` to your existing jupyterhub config (e.g. `/etc/jupyterhub/jupyterhub_config.py`)
4. Do not forget to change `c.JupyterHub.template_paths` to your public webpath
5. Restart your JupyterHub service
