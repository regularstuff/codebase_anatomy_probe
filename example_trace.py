from spiller import Spiller
import jinja2

template_create_spiller = Spiller()
jinja_snippet = "{% if score > 80 %} That's HUGE {% else %} So TINY {% endif %}"

template_create_spiller.start()
template = jinja2.environment.Environment().from_string(jinja_snippet)
template_create_spiller.stop()
template_create_spiller.start()

template_render_spiller = Spiller()
template_render_spiller.start()
template.render(score=100)
template_render_spiller.stop()

print(template_create_spiller.report(), flush=True)
print("-"*80, flush=True)
print(template_render_spiller.report(), flush=True)










