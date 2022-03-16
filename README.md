# diagram-as-code
manage diagrams as code

This repo contains proof-of-concept code to create diagrams from code.

Possible applications for this:
 - stop worrying about pixel-perfect alignment, focus on content
 - use the same layout for multiple environments / projects but with
   different names / values
 - make it possible to create diagrams with sanitized names suitable
   for public sharing
 - parse the output of another tool and generate a diagram
   (e.g. Terraform, Dynatrace, wiz.io)

Candidate:
 - https://diagrams.mingrammer.com
   concept code in python/mingrammer/
 - https://structurizr.org/             [python library potentially broken]
   (multiple languages supported)

related links:
 - https://alpha2phi.medium.com/code-based-diagramming-6b1bcc732aab
   Code-based Diagramming
 - https://mermaid.ink/ (can be integrated into GitHub documentation; different use case, did not pursue further)
 - draw.io (online editor, did not pursue further)
