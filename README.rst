Django Pipeline Eco
===================

django-pipeline-eco is a compiler for `django-pipeline <https://github.com/cyberdelia/django-pipeline>`_.

This compiler will produce a JS using the widely used JST model.

It basically compiles and appends to the window.JST JSON array the template that you request (through django-pipeline) using for example `Backbone.js <https://github.com/documentcloud/backbone>`_ or `Spine.js <https://github.com/maccman/spine>`_
.

Installation
~~~~~~~~~~~~
.. code-block:: sh

    pip install django-pipeline-eco

Add these lines in your django `settings.py`:

.. code-block:: python

    PIPELINE_JS = {
        'application': {
            'source_filenames': (
            	# Your other JS files...
                'path/to/your/templates/*.eco',
            ),
            'output_filename': 'js/application.js'
        }
    }

    PIPELINE_COMPILERS = (
        'pipeline_eco.compiler.EcoCompiler',
    )

Usage
~~~~~
If the paths are set correctly (try to play a bit depending on your static files situation), the eco will be compiled in a JS file and included automatically by pipeline.

You will just need then to call the rendered template using

.. code-block:: python

	Example.Views.Test = Backbone.View.extend
		template: "templates/example",

		render: (done) ->
			@el.innerHTML = JST[@template]

Deeply inspired by
~~~~~~~~~~~~~~~~~~
* `django-spine <https://github.com/ikeikeikeike/django-spine>`_ (base eco compiler) 
* `django-pipeline-compass <https://github.com/vbabiy/django-pipeline-compass>`_ (pipeline compiler model)