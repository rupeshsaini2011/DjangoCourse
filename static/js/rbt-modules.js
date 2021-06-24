(function ($) {
	$(window).load(function () {
		rbtAjax();
	});

	// ajax used to request php file
	function rbtAjax() {
		var rbtTheme = $('.rbt-toolbar').data("theme");
		var rbtFeatured = $('.rbt-toolbar').data("featured");
		var rbtButtonPosition = $('.rbt-toolbar').data("button-position");
		var rbtButtonHorizontal = $('.rbt-toolbar').data("button-horizontal");
		var rbtButtonAlt = $('.rbt-toolbar').data("button-alt");
		var rbtAso = getUrlParameter('aso');
		var rbtAca = getUrlParameter('aca');
		var rbtUtmCampaign = getUrlParameter('utm_campaign');
		var rbtReferrer = document.referrer;

		
	}

	function rbtLoadScript(url, onSuccess) {
		jQuery.ajax({
			url: url,
			dataType: 'script',
			success: onSuccess,
			async: true
		});
	}

	// lazy-load
	

	// open/close logic
	function rbtListToggle() {
		var opener = $('.rbt-theme-dropdown .rbt-btn'),
			list = $('.rbt-sidearea'),
			splitScreenPresent = typeof $.fn.multiscroll !== 'undefined' && typeof $.fn.multiscroll.setMouseWheelScrolling !== 'undefined';
			fullPagePresent = typeof $.fn.fullpage !== 'undefined' && typeof $.fn.fullpage.setMouseWheelScrolling !== 'undefined';

		var toggleList = function () {
			opener.on('click', function () {
				if (list.hasClass('rbt-active')) {
					list.removeClass('rbt-active');
					splitScreenPresent && $.fn.multiscroll.setMouseWheelScrolling(true);
					fullPagePresent && $.fn.fullpage.setMouseWheelScrolling(true);
				} else {
					list.addClass('rbt-active');
					splitScreenPresent && $.fn.multiscroll.setMouseWheelScrolling(false);
					fullPagePresent && $.fn.fullpage.setMouseWheelScrolling(false);
				}

				if (list.hasClass('rbt-scrolled')) {
					list.removeClass('rbt-scrolled');
				}
			});
		};

		var currentScroll = $(window).scrollTop();
		$(window).scroll(function () {
			var newScroll = $(window).scrollTop();
			if (Math.abs(newScroll - currentScroll) > 1000) {
				if (list.hasClass('rbt-active')) {
					list.removeClass('rbt-active');
					splitScreenPresent && $.fn.multiscroll.setMouseWheelScrolling(true);
					fullPagePresent && $.fn.fullpage.setMouseWheelScrolling(true);
				}

				if (!list.hasClass('rbt-scrolled')) {
					list.addClass('rbt-scrolled');
				}
			}
		});

		var clickAwayClose = function () {
			$(document).on('click', function (e) {
				if (!list.is(e.target) &&
					list.has(e.target).length === 0 &&
					list.hasClass('rbt-active')) {
					list.removeClass('rbt-active');
					splitScreenPresent && $.fn.multiscroll.setMouseWheelScrolling(true);
					fullPagePresent && $.fn.fullpage.setMouseWheelScrolling(true);
				}
			});
		};

		// init
		if (opener.length) {
			toggleList();
			clickAwayClose();
		}
	}

	// smooth-scroll compatibility
	function rbtSmoothScrollCompatibility() {
		var smoothScrollEnabled = $('body[class*="smooth-scroll"]').length || $('body[class*="smooth_scroll"]').length;

		if (smoothScrollEnabled && !$('html').hasClass('touch')) {
			var opener = $('.rbt-theme-dropdown .rbt-btn'),
				list = $('.rbt-sidearea');

			var disableScroll = function () {
				window.removeEventListener('mousewheel', smoothScrollListener, {passive: false});
				window.removeEventListener('DOMMouseScroll', smoothScrollListener, {passive: false});
			};

			var enableScroll = function () {
				window.addEventListener('mousewheel', smoothScrollListener, {passive: false});
				window.addEventListener('DOMMouseScroll', smoothScrollListener, {passive: false});
			};

			opener
				.on('click', function () {
					setTimeout(function () {
						list.hasClass('rbt-active') ? disableScroll() : enableScroll();
					}, 100);
				});

			list
				.on('mouseenter', function () {
					list.hasClass('rbt-active') && disableScroll();
				})
				.on('mouseleave', function () {
					enableScroll();
				});

		}
	}

	// initial load class
	function showList() {
		var list = $('.rbt-sidearea');

		list.length && list.addClass('rbt-loaded');
	}

	// get url parameter from url
	var getUrlParameter = function getUrlParameter(sParam) {
		var sPageURL = window.location.search.substring(1),
			sURLVariables = sPageURL.split('&'),
			sParameterName,
			i;

		for (i = 0; i < sURLVariables.length; i++) {
			sParameterName = sURLVariables[i].split('=');

			if (sParameterName[0] === sParam) {
				return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
			}
		}
	};
})(jQuery);