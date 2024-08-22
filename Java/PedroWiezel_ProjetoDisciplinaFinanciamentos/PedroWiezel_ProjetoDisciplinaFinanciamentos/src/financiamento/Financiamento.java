package financiamento;

import java.io.Serializable;

public abstract class Financiamento implements Serializable {

    private double valorImovel;
    private int prazoFinanciamento;
    private double taxaJurosAnual;
    private double valorTotal;

    public Financiamento(double valorImovel, int prazoFinanciamento, double taxaJurosAnual){
        this.valorImovel = valorImovel;
        this.prazoFinanciamento = prazoFinanciamento;
        this.taxaJurosAnual = taxaJurosAnual;
        this.valorTotal = calcular_total_pagamento();
    }

    public double getValorImovel(){
        return this.valorImovel;
    }
    public int getPrazoFinanciamento(){
        return this.prazoFinanciamento;
    }
    public double getTaxaJurosAnual(){
        return this.taxaJurosAnual;
    }
    public double calcular_valor_mensal(){
        return ((this.valorImovel / (this.prazoFinanciamento * 12)) * (1 + (this.taxaJurosAnual / 12)));
    }

    public double calcular_total_pagamento(){
        return (this.calcular_valor_mensal() * (this.prazoFinanciamento * 12));
    }

    public String imprimir_dados_financiamento() {
        String output = "";
        output += "Valor do imóvel: " + this.getValorImovel();
        output += "Valor total do financiamento: " + this.calcular_total_pagamento();
        output += "Valor da parcela mensal: " + this.calcular_valor_mensal();
        return output;
    }
}