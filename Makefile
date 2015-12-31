SERVICE_FLAG=
STATIC_SOURCE_PATH=docs/source
STATIC_DOCTREE_PATH=docs/build/doctrees
STATIC_HTML_PATH=docs/build/html
SCSS_PATH=static/scss
CSS_PATH=static/css
PIP_INSTALL=sudo -H pip install
DEPS=sphinx tornado flask jinja tori imagination kotoba sphinxcontrib-actdiag sphinxcontrib-blockdiag
REMOTE_UPDATE_CMD=ssh root@umi.shiroyuki.com "cd /data/com.shiroyuki.www && git pull && make web"

default:
	@echo 'Static command for NEP Core'
	@echo '  make service:  active the service'
	@echo '  make css:      compile CSS from SCSS'
	@echo '  make css_live: compile CSS from SCSS and update when a file is updated'
	@echo
	@echo 'For more options, run "./console".'

service: css
	@python server.py $(SERVICE_FLAG)

web:
	sphinx-build -b html -d $(STATIC_DOCTREE_PATH) $(STATIC_SOURCE_PATH) $(STATIC_HTML_PATH)

css:
	@sass --update $(SCSS_PATH):$(CSS_PATH) --style compressed

css-live:
	@sass --watch $(SCSS_PATH):$(CSS_PATH) --style compressed

install_deps:
	@${PIP_INSTALL} ${DEPS}

update_deps:
	@${PIP_INSTALL} -U ${DEPS}

remote_update:
	$(REMOTE_UPDATE_CMD)

deployment:
	git commit -am "Auto deployment"
	git push
	$(REMOTE_UPDATE_CMD)
