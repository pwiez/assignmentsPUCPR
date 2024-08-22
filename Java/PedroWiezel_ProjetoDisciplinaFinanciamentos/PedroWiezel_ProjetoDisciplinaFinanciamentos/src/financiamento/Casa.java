package financiamento;

import java.io.Serializable;

public class Casa extends Financiamento implements Serializable {

    private final static int TAXA_CASA_SEGURO = 80;

    private double tamanhoAreaConstruida;
    private double tamanhoTerreno;

    public Casa(double valorImovel, int prazoFinanciamento, double taxaJurosAnual, double tamanhoTerreno, double tamanhoAreaConstruida) {
        super(valorImovel, prazoFinanciamento, taxaJurosAnual);
        this.tamanhoAreaConstruida = tamanhoAreaConstruida;
        this.tamanhoTerreno = tamanhoTerreno;
    }

    @Override
    public double calcular_valor_mensal(){
        return ((this.getValorImovel() / (this.getPrazoFinanciamento() * 12)) * (1 + ((this.getTaxaJurosAnual() / 12) / 100 ))) + TAXA_CASA_SEGURO;
    }

    public double getTamanhoAreaConstruida() {
        return tamanhoAreaConstruida;
    }

    public void setTamanhoAreaConstruida(double tamanhoAreaConstruida) {
        this.tamanhoAreaConstruida = tamanhoAreaConstruida;
    }

    public double getTamanhoTerreno() {
        return tamanhoTerreno;
    }

    public void setTamanhoTerreno(double tamanhoTerreno) {
        this.tamanhoTerreno = tamanhoTerreno;
    }

    @Override
    public String imprimir_dados_financiamento() {
        String output = "";
        output += "Valor do imóvel: " + this.getValorImovel() + "\n";
        output += "Valor total do financiamento: " + this.calcular_total_pagamento() + "\n";
        output += "Valor da parcela mensal: " + this.calcular_valor_mensal() + "\n";
        output += "Tamanho do terreno: " + this.tamanhoTerreno + "\n";
        output += "Tamanho da área construída: " + this.tamanhoAreaConstruida + "\n";
        output += "-------------------------\n";
        return output;
    }
}
