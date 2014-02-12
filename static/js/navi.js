/*! Eryri Educational Platform - UI Component | v0.2 | (C) Juti Noppornpitak and eryri-web contributors | MIT License */
"use strict";

var EryriOffCanvasNavigation = function (elementOrJQuery) {
    this.$nav     = $(elementOrJQuery);
    this.$wrapper = this.$nav.closest('.off-canvas-wrapper');
};

EryriOffCanvasNavigation.prototype.$body = $('body');

EryriOffCanvasNavigation.prototype.enable = function () {
    if (this.$nav.hasClass('enabled')) {
        return;
    }

    this.$nav.on('click', '.activator', $.proxy(this.onActivatorClicked, this));
    this.$nav.on('click', '.deactivator', $.proxy(this.onDeactivatorClicked, this));

    this.$nav.addClass('enabled');
};

EryriOffCanvasNavigation.prototype.onActivatorClicked = function (e) {
    e.preventDefault();

    this.$nav.addClass('activated');
    this.$wrapper.addClass('activated');
    this.$body.addClass('off-canvas-horizon');
};

EryriOffCanvasNavigation.prototype.onDeactivatorClicked = function (e) {
    e.preventDefault();

    this.$nav.removeClass('activated');
    this.$wrapper.removeClass('activated');
    this.$body.removeClass('off-canvas-horizon');
};

// Auto initialization
$(function () {
    $('nav.off-canvas').each(function (index) {
        var navigator = new EryriOffCanvasNavigation(this);

        navigator.enable();
    });
});