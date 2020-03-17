{% extends 'python.tpl'%}
## remove markdown cells
{% block markdowncell %}{% endblock markdowncell %}
## remove execution count
{% block in_prompt %}{% endblock in_prompt %}
