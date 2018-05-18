IP ?= IP
VERSION ?= 5.7.20

ROOT := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

RPMBUILD = $(ROOT)/rpmbuild
RPMS = $(RPMBUILD)/RPMS
SOURCES = $(RPMBUILD)/SOURCES
SPECS = $(RPMBUILD)/SPECS

SPEC_SRC = $(ROOT)/unifi.spec
SPEC = $(SPECS)/unifi.spec
ZIP_SRC = $(HOME)/annex/software/unifi-$(VERSION).zip
ZIP = $(SOURCES)/unifi-$(VERSION).zip

default : $(SPEC) $(ZIP)
	$(ROOT)/remote-build $(RPMBUILD) $(IP)

$(SPEC) : $(SPEC_SRC)
	mkdir -p $(SPECS)
	cp $(SPEC_SRC) $(SPEC)

$(ZIP) : $(ZIP_SRC)
	mkdir -p $(SOURCES)
	cp $(ZIP_SRC) $(ZIP)
