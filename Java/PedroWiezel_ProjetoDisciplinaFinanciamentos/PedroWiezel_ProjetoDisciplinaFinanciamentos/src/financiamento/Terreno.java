package financiamento;

import java.io.Serializable;

public class Terreno extends Financiamento implements Serializable {

    private static final double TAXA_EXTRA = 1.02;
    private String zona;

    public Terreno(double valorImovel, int prazoFinanciamento, double taxaJurosAnual, String zona) {
        super(valorImovel, prazoFinanciamento, taxaJurosAnual);
        this.zona = zona;
    }

    @Override
    public double calcular_valor_mensal(){
        return ((this.getValorImovel() / (this.getPrazoFinanciamento() * 12))
                * (1 + ((this.getTaxaJurosAnual() / 12) / 100))) * TAXA_EXTRA;
    }

    public String getZona() {
        return zona;
    }

    public void setZona(String zona) {
        this.zona = zona;
    }

    @Override
    public String imprimir_dados_financiamento() {
        String output = "";
        output += "Valor do imóvel: " + this.getValorImovel() + "\n";
        output += "Valor total do financiamento: " + this.calcular_total_pagamento() + "\n";
        output += "Valor da parcela mensal: " + this.calcular_valor_mensal() + "\n";
        output += "Zona: " + this.zona + "\n";
        output += "-------------------------\n";
        return output;
    }
}
