from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device="cuda")

ARTICLE = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
2010 marriage license application, according to court documents.
Prosecutors said the marriages were part of an immigration scam.
On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
"""

ARTICLE2 = """ Maria da Fonte, ou Revolta do Minho, foi uma revolta popular ocorrida na primavera de 1846 contra o governo cartista presidido por António Bernardo da Costa Cabral.

A revolta resultou das tensões sociais remanescentes das guerras liberais, exacerbadas pelo grande descontentamento popular gerado pelas novas leis de recrutamento militar que se lhe seguiram, por alterações fiscais e pela proibição de realizar enterros dentro de igrejas.

Iniciou-se na zona de Póvoa de Lanhoso (Minho) uma sublevação popular que se foi progressivamente estendendo a todo o norte de Portugal. A instigadora dos motins iniciais terá sido uma mulher do povo chamada Maria, natural da freguesia de Fontarcada, que por isso ficaria conhecida pela alcunha de Maria da Fonte. Como a fase inicial do movimento insurreccional teve uma forte componente feminina, acabou por ser esse o nome dado à revolta.

A sublevação propagou-se depois ao resto do país e provocou a substituição do governo de Costa Cabral por um presidido por Pedro de Sousa Holstein, o 1.º Duque de Palmela. Quando, num golpe palaciano, conhecido pela Emboscada, a 6 de outubro daquele ano, a rainha D. Maria II demite o governo e nomeia o marechal João Carlos de Saldanha Oliveira e Daun, 1.º Duque de Saldanha, para constituir novo ministério, a insurreição reacende-se.

O resultado foi uma nova guerra civil de 8 meses, a Patuleia, que apenas terminaria com a assinatura da Convenção de Gramido, a 30 de junho de 1847, após a intervenção de forças militares estrangeiras ao abrigo da Quádrupla Aliança. 
"""

print(summarizer(ARTICLE2, max_length=130, min_length=30, do_sample=False))
