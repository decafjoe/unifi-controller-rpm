IP ?= IP
VERSION ?= 5.7.20

ROOT := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

RPMBUILD = $(ROOT)/rpmbuild
RPMS = $(RPMBUILD)/RPMS
SOURCES = $(RPMBUILD)/SOURCES
SPECS = $(RPMBUILD)/SPECS

EXE_SRC = $(ROOT)/unifid
EXE = $(SOURCES)/unifid
INIT_SRC = $(ROOT)/unifid.init
INIT = $(SOURCES)/unifid.init
SPEC_SRC = $(ROOT)/unifi.spec
SPEC = $(SPECS)/unifi.spec
ZIP_SRC = $(HOME)/annex/software/unifi-$(VERSION).zip
ZIP = $(SOURCES)/unifi-$(VERSION).zip

default : $(EXE) $(INIT) $(SPEC) $(ZIP)
	$(ROOT)/remote-build $(RPMBUILD) $(IP)

$(EXE) : $(EXE_SRC)
	mkdir -p $(SOURCES) && cp $(EXE_SRC) $(EXE)

$(INIT) : $(INIT_SRC)
	mkdir -p $(SOURCES) && cp $(INIT_SRC) $(INIT)

$(SPEC) : $(SPEC_SRC)
	mkdir -p $(SPECS) && cp $(SPEC_SRC) $(SPEC)

$(ZIP) : $(ZIP_SRC)
	mkdir -p $(SOURCES) && cp $(ZIP_SRC) $(ZIP)
